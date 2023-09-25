import base64
import datetime
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from django.core.files.base import ContentFile
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appuser 
        fields = ('userid', 'useremail', 'password', 'savedate', 'userroleid')
    
class PersonalSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalsalud 
        fields = ('cedulamed', 'nombresmed', 'apellidosmed', 'telefonomed', 'direccionmed', 'userid', 'hospitalid')
        
class UsuarioExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarioexterno 
        fields = ('cedulaext', 'nombresext', 'apellidosext', 'telefonoext', 'direccionext', 'userid', 'institutionid')
        
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
        
class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta 
        fields = ('consultaid', 'fecha_consulta', 'motivo_consulta', 'medConsulta', 'medUltrasonido', 'idpac', 'idembarazo')
        
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('idpac', 'cedulapac', 'apellido_materno', 'apellido_paterno', 'nombreuno', 'nombredos', 'fechanac', 'numgestacion', 'lmp')
        
class FetoMedicionDiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FetoMedicionDiagnostico
        fields =  'reporte', 'hc_hadlock', 'bpd_hadlock', 'csp', 'cm', 'vp', 'va', 'cereb_hill', 'efw', 'afi',

class EmbarazoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embarazo
        fields = '__all__'

class FetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feto
        fields =  'id_embarazo', 'posicion_feto'
        
class ImagesSerializer(serializers.ModelSerializer):
    image_data = serializers.FileField(required=True)
    
    class Meta:
        model = Images
        fields = ['image_data', 'reporte']
        
    def save(self):
        image_data = self.validated_data['image_data']
        reporte = self.validated_data['reporte']
        gaweeks = self.context.get('gaweeks')
        
        print("--------------------------------------------")
        print("imagedata", image_data, "reporte", reporte, "gaweeks", gaweeks)
        mymodel = Images(image_data=image_data, reporte=reporte)
        print("model", mymodel)
        options_dict = {"Metadata": {"sexo": "", 
                                    "ga": gaweeks,
                                    "tipo_examen": "NEUROSONOGRAFIA",
                                    "hallazgo": ""}
                        } 
        mymodel.image_data.storage.object_parameters.update(options_dict)
        mymodel.save()