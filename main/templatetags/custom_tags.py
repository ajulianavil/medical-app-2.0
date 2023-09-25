from django import template
from main.models import Personalsalud, Usuarioexterno, Hospital, Institucion, Embarazo, Feto, Consulta, Reporte, FetoMedicionDiagnostico
from users.models import Appuser

register = template.Library()

@register.simple_tag
def get_medico_name(cedulamed):
    medico = Personalsalud.objects.get(cedulamed=cedulamed)
    first_name = medico.nombresmed.split(' ')[0] if ' ' in medico.nombresmed else medico.nombresmed
    last_name = medico.apellidosmed.split(' ')[0] if ' ' in medico.apellidosmed else medico.apellidosmed
    full_name = f'{first_name} {last_name}'
    return full_name  # Replace 'name' with the actual field you want to retrieve

@register.simple_tag
def get_medico_id(cedulamed):
    medico = Personalsalud.objects.get(cedulamed=cedulamed).userid_id
    user = Appuser.objects.get(userid = medico)
    
    return user.userid  # Replace 'name' with the actual field you want to retrieve


@register.simple_tag
def get_info_user(userid):
    medico_data = Personalsalud.objects.filter(userid=userid).first()
    investigador_data = Usuarioexterno.objects.filter(userid=userid).first()
    cedula = None
    telefono = None
    direccion = None
    institucion = None
    
    if medico_data != None:
        cedula = medico_data.cedulamed
        telefono = medico_data.telefonomed
        direccion = medico_data.direccionmed
        institucion = Hospital.objects.get(id = medico_data.hospitalid_id).nombrehospital

    elif investigador_data != None:
        cedula = investigador_data.cedulaext
        telefono = investigador_data.telefonoext
        direccion = investigador_data.direccionext
        institucion = Institucion.objects.get(institucionid = investigador_data.institutionid_id).nombreinstitucion
    
    if cedula:
        return cedula, telefono, direccion, institucion  # Replace 'name' with the actual field you want to retrieve
    else:
        return '----'

@register.simple_tag
def get_embarazo(embarazoid):
    numero_embarazo = None
    embarazo = Embarazo.objects.get(id_embarazo = embarazoid)
    numero_embarazo = embarazo.numero_embarazo
    multiple = Feto.objects.filter(id_embarazo = embarazoid).count()
    
    if multiple > 0:
        is_multiple = f'Múltiple - {multiple}'
    else:
        is_multiple = 'Único'
    return numero_embarazo, is_multiple

@register.simple_tag
def get_estado(consultaid):

    reportes = Reporte.objects.filter(consultaid = consultaid)
    
    record_count_normal = 0
    record_count_anormal = 0
    for reporte in reportes:
        diagnostico = FetoMedicionDiagnostico.objects.filter(reporte = reporte.idreporte)
        
        for instance in diagnostico:
            for field in instance._meta.get_fields():
                if field.name not in ['idfetomediciondiagnostico', 'reporte']:
                    value = getattr(instance, field.name)

                    if value == 'Normal':
                        record_count_normal += 1
                        next;
                    else:
                        record_count_anormal += 1
                        break;
    
    if record_count_anormal > 0:
        estado = 'Con anormalidades'
    else:
        estado = 'En rangos normales'
    return estado
    
            