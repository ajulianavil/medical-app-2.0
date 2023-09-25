import csv
from datetime import datetime
import io
import json

from django.http import HttpResponse
from django.http import FileResponse
from main.models import *

def get_matching_consulta(consulta_id):
    matching_consulta = Consulta.objects.filter(consultaid=consulta_id).first()
    formatted_date = datetime.strftime(matching_consulta.fecha_consulta,'%Y/%m/%d')
    formatted_hora = datetime.strftime(matching_consulta.fecha_consulta,'%H:%M')
    matching_consulta.formatted_fecha_consulta = formatted_date
    matching_consulta.formatted_hora_consulta = formatted_hora
    
    matching_patient = Paciente.objects.filter(idpac=matching_consulta.idpac_id).first()
    # matching_clinichist = Historiaclinica.objects.filter(idPaciente=matching_patient.idpac).first()
    matching_report = Reporte.objects.filter(consultaid=matching_consulta.consultaid)
    matching_result_info = []
    if(len(matching_report)>1):
        for r in matching_report:
            diagnostico = FetoMedicionDiagnostico.objects.filter(reporte=r.idreporte).first()
            matching_result_info.append(diagnostico)
    else:
        for reporte in matching_report:
            diagnostico = FetoMedicionDiagnostico.objects.filter(reporte=reporte.idreporte).first()
            matching_result_info.append(diagnostico)
    
    return matching_consulta, matching_patient, matching_report, matching_result_info


def get_mediciones():
    return  {
        'hc_hadlock': 1,
        'bpd_hadlock': 2,
        'csp': 3,
        'cm': 4,
        'vp': 5,
        'va': 6,
        'cereb_hill': 7,
        'afi': 8,
        'efw': 9
    }
