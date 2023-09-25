import datetime
from django import template
from django.conf import settings
from users.context_processors import current_user

from main.models import *

register = template.Library()

@register.filter
def get_array_object(array, index):
    if index < len(array):
        return array[index]
    else:
        return None

@register.filter
def get_fields(obj):
    return obj._meta.get_fields()

@register.filter
def get_field_value(item, field):
    prefixed_attr = field + '_1'
    if hasattr(item, prefixed_attr):
        value = getattr(item, prefixed_attr)
        return value
    else:
        if hasattr(item, field):
            value = getattr(item, field)
            return value
        else:
            return None

@register.filter
def get_ga(id):
    reporte = Reporte.objects.filter(consultaid = id).first()
    reporte_ga = reporte.ga 
    if reporte_ga:
        return reporte_ga
    else:
        return '0'

@register.filter
def get_med_name(item):
    convertidorDeMediciones = {
        'hc_hadlock': 'Circunferencia de la cabeza (HC_HADLOCK)',
        'bpd_hadlock': 'Diámetro biparietal (BPD_HADLOCK)',
        'cereb_hill' : 'Diámetro transverso del cerebelo (CEREB_HILL)',
        'efw' : 'Peso estimado fetal (EFW)',
        'csp': 'Cavum septumpellucidum (CSP)',
        'cm':'Cisterna Magna (CM)',
        'vp':'Ventrículo posterior (VP)',
        'va':'Ventrículo anterior (VA)',
        'afi':'Indice de líquido amniótico (AFI)',
    }
    return convertidorDeMediciones[item]

@register.filter
def get_med_name_nosiglas(item):
    convertidorDeMediciones = {
        'hc_hadlock': 'Circunferencia de la cabeza',
        'bpd_hadlock': 'Diámetro biparietal',
        'cereb_hill' : 'Diámetro transverso del cerebelo',
        'efw' : 'Peso estimado fetal',
        'csp': 'Cavum septumpellucidum',
        'cm':'Cisterna Magna',
        'vp':'Ventrículo posterior',
        'va':'Ventrículo anterior',
        'afi':'Indice de líquido amniótico',
    }
    return convertidorDeMediciones[item]

@register.filter
def get_ref_values(reporte, medicion):
    
    tipo_medicion = Tipomedicion.objects.get(nombreMedicion = medicion.upper())
    idMedicion = tipo_medicion.idTipoMedicion
    
    if medicion == 'efw' or medicion == 'afi':
        reporte_value = Reporte.objects.get(idreporte=reporte.idreporte)
        value = getattr(reporte_value, medicion)
    else:
        reporte_value = Reporte.objects.get(idreporte=reporte.idreporte)
        prefixed_attr = medicion + '_1'
        value = getattr(reporte_value, prefixed_attr)
        
    if idMedicion == 1 or idMedicion == 2 or idMedicion == 3:
        try:
            med = Medicion.objects.get(id_tipo_medicion=idMedicion, ga=reporte.ga)
        
            if float(med.valormin) < float(value) < float(med.valorinter):
                return ' en el rango ' + str(med.valormin) + ' - ' + str(med.valorinter)
            else:
                return ' fuera del rango ' + str(med.valormin) + ' - ' + str(med.valorinter)
        except Medicion.DoesNotExist:
            med = None
            return '(No se hallaron valores de referencia)'
    
    if idMedicion == 7:
        try:
            med = Medicion.objects.get(id_tipo_medicion=idMedicion, ga=reporte.ga)
            if float(med.valormin) < float(value):
                return ' en el rango > ' + str(med.valormin)
            else:
                return ' en del rango < ' + str(med.valormin)
        except Medicion.DoesNotExist:
            med = None
            return '(No se hallaron valores de referencia)'

    if idMedicion == 4:
        if float(settings.CM_REF) < float(value):
            return ' fuera del rango < ' + str(settings.CM_REF)
        else:
            return ' en el rango < ' + str(settings.CM_REF)

    if idMedicion == 5 or idMedicion == 6:
        if float(value) < float(settings.VT_MIN):
            return ' en el rango < ' + str(settings.VT_MIN)
        
        if  float(settings.VT_1) < float(value) < float(settings.VT_2):
            return ' en el rango ' + str(settings.VT_1) + ' - ' + str(settings.VT_2)
        
        if float(settings.VT_3) < float(value) < float(settings.VT_4):
            return ' en el rango ' + str(settings.VT_3) + ' - ' + str(settings.VT_4)
        
        if float(value) > float(settings.VT_MAX):
            return ' en el rango > ' + str(settings.VT_MAX)
                        
    if idMedicion == 8:
        if float(value) < float(settings.AFI_MIN):
            return ' en el rango < ' + str(settings.AFI_MIN)
        
        if  float(settings.AFI_MIN) < float(value) < float(settings.AFI_MAX):
            return  ' en el rango ' + str(settings.AFI_MIN) + ' - ' + str(settings.AFI_MAX)
        
        if float(value) > float(settings.AFI_MAX):
            return   ' en el rango > ' + str(settings.AFI_MAX)
        
    if idMedicion == 9:
        try:
            med = Medicion.objects.get(id_tipo_medicion=idMedicion, ga=reporte.ga)

            print(med, med.valordev, value, med.valorinter)
            if float(med.valordev) < float(value) < float(med.valorinter):
                return ' en el rango ' + str(med.valormin) + ' - ' + str(med.valorinter)
            else:
                return ' fuera del rango ' + str(med.valordev) + ' - ' + str(med.valorinter)
        except Medicion.DoesNotExist:
            med = None
            return '(No se hallaron valores de referencia)'
        
    
    
@register.filter
def get_ref_values_pdf(reporte, medicion):
    try:
        tipo_medicion = Tipomedicion.objects.get(nombreMedicion = medicion.upper())
        idMedicion = tipo_medicion.idTipoMedicion
        med = Medicion.objects.get(id_tipo_medicion=idMedicion, ga=reporte.ga)
        
        if medicion == 'efw' or medicion == 'afi':
            reporte_value = Reporte.objects.get(idreporte=reporte.idreporte)
            value = getattr(reporte_value, medicion)
        else:
            reporte_value = Reporte.objects.get(idreporte=reporte.idreporte)
            prefixed_attr = medicion + '_1'
            value = getattr(reporte_value, prefixed_attr)

        if idMedicion == 1 or idMedicion == 2 or idMedicion == 7 or idMedicion == 3 or idMedicion == 9:
            return str(med.valormin) + ' - ' + str(med.valorinter)
        
        # if idMedicion == 7:
        #     if float(med.valormin) < float(value):
        #         return str(med.valormin)
        #     else:
        #         return str(med.valormin)

        if idMedicion == 4:
            return ' < ' + str(settings.CM_REF)
        if idMedicion == 5 or idMedicion == 6:
                return ' < ' + str(settings.VT_MIN)
            # if float(value) < float(settings.VT_MIN):
                
            # if  float(settings.VT_1) < float(value) < float(settings.VT_2):
            #     return str(settings.VT_1) + ' - ' + str(settings.VT_2)
            
            # if float(settings.VT_3) < float(value) < float(settings.VT_4):
            #     return str(settings.VT_3) + ' - ' + str(settings.VT_4)
            
            # if float(value) > float(settings.VT_MAX):
            #     return + str(settings.VT_MAX)
                            
        if idMedicion == 8:
                return ' < ' + str(settings.AFI_MIN)
            # if float(value) < float(settings.AFI_MIN):
                
            # if  float(settings.AFI_MIN) < float(value) < float(settings.AFI_MAX):
            #     return  str(settings.AFI_MIN) + ' - ' + str(settings.AFI_MAX)
            
            # if float(value) > float(settings.AFI_MAX):
            #     return   + str(settings.AFI_MAX)
        
    except Medicion.DoesNotExist:
        med = None
        return '(No existen valores de referencia)'

@register.filter
def get_diagnosis(reporte, medicion):
    diagnosis = FetoMedicionDiagnostico.objects.get(reporte=reporte)
    for field in diagnosis._meta.get_fields():
        if field.name == medicion:
            field_value = getattr(diagnosis, field.name)
            return field_value

@register.filter
def get_diagnosis_conclude(reporte, medicion):
    diagnosis = FetoMedicionDiagnostico.objects.get(reporte=reporte)
    for field in diagnosis._meta.get_fields():
        if field.name == medicion:
            field_value = getattr(diagnosis, field.name)
            if field.name == 'bpd_hadlock' or field.name == 'csp' or field.name == 'vp' or field.name == 'va':
                return field_value + ' (' + field.name + ')'
            else:
                return field_value
            
@register.filter
def get_pacient_id(id:int):
    pacient = Paciente.objects.filter(idpac=id)
    if pacient:
        for item in pacient:
            idpac = item.cedulapac
        return idpac
    else:
        notFount = 'Sin cédula'
        return notFount                  

@register.filter
def get_numero_embarazo(id_embarazo):
    embarazo = Embarazo.objects.filter(id_embarazo=id_embarazo)
    if embarazo:
        for item in embarazo:
            numero_embarazo = item.numero_embarazo
        return numero_embarazo
    else:
        notFount = '0'
        return notFount     

@register.filter
def total_pacientes(id:int):
    record_count = 0;
    current_month = datetime.datetime.now().month
    consulta_mes = Consulta.objects.filter(fecha_consulta__month=current_month, medConsulta=id)
    
    record_count = consulta_mes.count()
    return record_count

@register.filter
def total_fetos(id:int):
    total_count = 0
    
    current_month = datetime.datetime.now().month
    consulta_mes = Consulta.objects.filter(fecha_consulta__month=current_month, medConsulta=id)
    for consulta in consulta_mes:
        record_count_normal = 0;  
        reporte = Reporte.objects.filter(consultaid = consulta.consultaid)

        for r in reporte:
            diagnostico = FetoMedicionDiagnostico.objects.filter(reporte = r.idreporte)
            
            for instance in diagnostico:
                for field in instance._meta.get_fields():
                    if field.name not in ['idfetomediciondiagnostico', 'reporte']:
                        value = getattr(instance, field.name)

                        if value == 'Normal':
                            record_count_normal += 1
                            next;
                        else:
                            break
                
                if record_count_normal == 9:
                    total_count += 1
            
    return total_count

@register.filter
def total_anormales(id:int):
    record_count_anormal = 0;
    
    current_month = datetime.datetime.now().month
    consulta_mes = Consulta.objects.filter(fecha_consulta__month=current_month, medConsulta=id)
    
    for consulta in consulta_mes:
        reporte = Reporte.objects.filter(consultaid = consulta.consultaid)

        for r in reporte:
            diagnostico = FetoMedicionDiagnostico.objects.filter(reporte = r.idreporte)
        
            for instance in diagnostico:
                for field in instance._meta.get_fields():
                    if field.name not in ['idfetomediciondiagnostico', 'reporte']:
                        value = getattr(instance, field.name)

                        if value == 'Normal':
                            next;
                        else:
                            record_count_anormal += 1
                            break
                    
    return record_count_anormal

@register.filter
def get_last_consult(id:int):
    consulta = Consulta.objects.filter(medConsulta=id).last()
    if consulta:
        return consulta
