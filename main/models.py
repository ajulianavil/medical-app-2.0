from django.db import models
from django.utils import timezone

from users.models import Appuser
from .validators import val_cedulamed, val_cedulaext, val_cedulapac, validate_unique_user_identification, validate_unique_phone
# from tinymce.models import HTMLField

# Create your models here.
class Hospital(models.Model):
    nombrehospital = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=150)
    departamento = models.CharField(max_length=150)

    def __str__ (self):
        return self.nombrehospital
    
    class Meta:
        db_table = 'Hospital'
        verbose_name_plural = "Hospitales"
        ordering = ['nombrehospital']

class Personalsalud(models.Model):
    cedulamed = models.IntegerField( primary_key=True, validators=[val_cedulamed, validate_unique_user_identification])  # Field name made lowercase.
    nombresmed = models.CharField( max_length=150)  # Field name made lowercase.
    apellidosmed = models.CharField( max_length=150)  # Field name made lowercase.
    telefonomed = models.CharField(max_length=50,  unique=True, validators=[validate_unique_phone])  # Field name made lowercase.
    direccionmed = models.CharField(max_length=200)  # Field name made lowercase.
    userid = models.ForeignKey(Appuser, on_delete=models.SET_DEFAULT, default="")  # Field name made lowercase.
    hospitalid = models.ForeignKey(Hospital, default="", verbose_name= "Hospitales", on_delete=models.SET_DEFAULT)  # Field name made lowercase.
    
    def __str__ (self):
        return str(self.cedulamed)
    
    class Meta:
        db_table = 'PersonalSalud'
        verbose_name_plural = "Personal"
        ordering = ['cedulamed']

class Paciente(models.Model):
    idpac = models.AutoField(db_column='idPac', primary_key=True)  # Field name made lowercase.
    cedulapac = models.IntegerField(db_column='cedulaPac', blank=True, null=True, validators=[val_cedulapac], unique=True)  # Field name made lowercase.
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=100, blank=True, null=True)
    nombreuno = models.CharField(db_column='nombreUno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombredos = models.CharField(db_column='nombreDos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechanac = models.CharField(db_column='fechaNac', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numgestacion = models.IntegerField(db_column='numGestacion', blank=True, null=True)  # Field name made lowercase.
    lmp = models.CharField(db_column='LMP', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta: 
        verbose_name_plural = "Pacientes"
        db_table = 'Paciente'

class Institucion(models.Model):
    institucionid = models.IntegerField(db_column='institucionId', primary_key=True)  # Field name made lowercase.
    nombreinstitucion = models.CharField(db_column='nombreInstitucion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(max_length=150, blank=True, null=True)
    departamento = models.CharField(max_length=150, blank=True, null=True)

    def __str__ (self):
            return self.nombreinstitucion
    
    class Meta:
        verbose_name_plural = "Instituciones"
        db_table = 'Institucion'

class Usuarioexterno(models.Model):
    cedulaext = models.IntegerField( primary_key=True, validators=[val_cedulaext, validate_unique_user_identification])  # Field name made lowercase.
    nombresext = models.CharField( max_length=150, blank=True, null=True)  # Field name made lowercase.
    apellidosext = models.CharField( max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefonoext = models.CharField( max_length=50, blank=True, null=True, validators=[validate_unique_phone])  # Field name made lowercase.
    direccionext = models.CharField( max_length=200, blank=True, null=True)  # Field name made lowercase.
    userid = models.OneToOneField(Appuser, models.SET_DEFAULT, db_column='UserId', default="", unique=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institucion, models.SET_DEFAULT, default="")  # Field name made lowercase.

    class Meta:
        verbose_name_plural = "UsuariosExternos"
        db_table = "UsuarioExterno"

class Embarazo(models.Model):
    id_embarazo = models.AutoField( primary_key=True)
    idpac = models.ForeignKey(Paciente, models.SET_DEFAULT, default="")  # Field name made lowercase.
    numero_embarazo = models.PositiveIntegerField(default=0)
   
    class Meta:
        db_table = 'Embarazo'
        verbose_name_plural = 'Embarazos'

class Feto(models.Model):
    idfeto = models.AutoField( primary_key=True)
    id_embarazo = models.ForeignKey(Embarazo, on_delete=models.CASCADE)
    posicion_feto = models.CharField( max_length=1000, blank=True, null=True)  # Field name made lowercase.
    
    def __str__ (self):
        return str(self.idfeto)
    
    class Meta:
        db_table = 'Feto'
        verbose_name_plural = 'Fetos'

class Consulta(models.Model):
    consultaid = models.AutoField(primary_key=True)
    fecha_consulta = models.DateTimeField()
    motivo_consulta = models.CharField(max_length=1000, default='Ultrasonido de control')
    medConsulta = models.ForeignKey(Personalsalud, models.SET_DEFAULT, default="", blank=True, null=True) #ESTO DEBERIA IR ENLAZADO A USER
    medUltrasonido = models.CharField(max_length=200, blank=True, null=True)  # Field name made lowercase.# Field name made lowercase.
    idpac = models.ForeignKey(Paciente, models.SET_DEFAULT, default="")  # Field name made lowercase.
    idembarazo = models.ForeignKey(Embarazo, models.SET_DEFAULT, default="", null=True)

    def __str__ (self):
        return str(self.consultaid)
    
    @property
    def consulta(self):
        return self.medConsulta.nombresmed + "/" + self.consultaid

    class Meta:
        db_table = 'Consulta'
        verbose_name_plural = "Consultas"
        ordering = ['consultaid']


class Tipomedicion(models.Model):
    idTipoMedicion = models.AutoField( primary_key=True)  # Field name made lowercase.
    nombreMedicion = models.CharField( max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'TipoMedicion'
        verbose_name_plural = "TiposMedicion"
        

class Medicion(models.Model):
    idmedicion = models.AutoField(db_column='idMedicion', primary_key=True)  # Field name made lowercase.
    ga = models.IntegerField(db_column='ga', null=False, blank=False)
    valormin = models.FloatField(db_column='valorMin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valorinter = models.FloatField(db_column='valorMax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valordev = models.FloatField(db_column='valorDev', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_tipo_medicion = models.ForeignKey(Tipomedicion, on_delete=models.SET_DEFAULT, default="", db_column='idTipoMedicion', blank=False, null=False)
    
    class Meta:
        db_table = 'Medicion'
        verbose_name_plural = "Mediciones"

class Reporte(models.Model):
    idreporte = models.AutoField(db_column='idReporte', primary_key=True)  # Field name made lowercase.
    consultaid = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    fetoid = models.ForeignKey(Feto, on_delete=models.CASCADE, blank=True, null=True)
    efw = models.CharField(max_length=100, blank=True, null=True)
    edb = models.CharField(max_length=100, blank=True, null=True)
    ga = models.CharField(max_length=100, blank=True, null=True)
    csp_1 = models.CharField(max_length=50, blank=True, null=True)
    cm_1 = models.CharField(max_length=50, blank=True, null=True)
    hc_hadlock_1 = models.CharField(max_length=50, blank=True, null=True)
    bpd_hadlock_1 = models.CharField(max_length=50, blank=True, null=True)
    cereb_hill_1 = models.CharField(max_length=50, blank=True, null=True)
    va_1 = models.CharField(max_length=50, blank=True, null=True)
    vp_1 = models.CharField(max_length=50, blank=True, null=True)
    ga_days = models.CharField(max_length=100, blank=True, null=True)
    afi = models.CharField(max_length=50, blank=True, null=True)
    txtresults = models.CharField( max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Reporte'
        verbose_name_plural = "Reportes"

class FetoMedicionDiagnostico(models.Model):
    idfetomediciondiagnostico = models.AutoField( primary_key=True)  # Field name made lowercase.
    reporte = models.ForeignKey(Reporte, models.CASCADE, default="")  # Field name made lowercase.
    hc_hadlock = models.CharField( max_length=100,db_column='hc_hadlock',null=False, blank=False, default="",)
    bpd_hadlock = models.CharField( max_length=100,db_column='bpd_hadlock',null=False, blank=False, default="",)
    cm = models.CharField( max_length=100,db_column='cm',null=False, blank=False, default="",)
    vp = models.CharField( max_length=100,db_column='vp',null=False, blank=False, default="",)
    va = models.CharField( max_length=100,db_column='va',null=False, blank=False, default="",)
    afi = models.CharField( max_length=100,db_column='afi',null=False, blank=False, default="",)
    cereb_hill = models.CharField( max_length=100,db_column='cereb_hill',null=False, blank=False, default="",)
    efw = models.CharField( max_length=100,db_column='efw',null=False, blank=False, default="",)
    csp = models.CharField( max_length=100,db_column='csp',null=False, blank=False, default="",)

    class Meta:
        db_table = 'FetoMedicionDiagnostico'
        verbose_name_plural = "FetoMedicionDiagnostico"
        
class Images(models.Model):
    idimage = models.BigAutoField(primary_key=True)
    image_data = models.FileField(upload_to='ultrasond_images/')
    reporte = models.ForeignKey(Reporte, models.CASCADE, default="")  # Field name made lowercase.
    