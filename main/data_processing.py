from django.conf import settings
from django.shortcuts import render
import numpy as np
import re
from django.contrib import messages


from main.models import Medicion, Tipomedicion

def process_data(file):
    file_readed = file.readlines()
    studydate = None  # Assign default value to studydate
    studytime = None
    pat_id = None
    pat_lastname = None
    pat_name = None
    num_gesta = None
    lmp = None
    EFW = 0
    CLINICAL_EDC = None
    ga_weeks = None
    csp_1 = 0
    cm_1 = 0
    hc_hadlock_1 = 0
    bpd_hadlock_1 = 0
    cereb_hill_1 = 0
    va_1 = 0
    vp_1 = 0
    ga_days = None
    afi_sum = None
    med_name = None
    med_lastname = None
    comments = ""
    insert_paciente = {}
    reporte_info = {}
    
    count = 0
    try:
        for row_bytes in file_readed:
            row = row_bytes.decode("utf-8") 
            if ('STUDYDATE' in row):
                studydate = row.strip().split(" ")[1]
            elif ('STUDYTIME' in row):
                studytime = row.strip().split(" ")[1]
            elif ('HOSPITAL' in row):
                hospital = row.strip().split(" ")[1]
                hospital = hospital[1:]
                hospital = hospital[:-1]
            elif ('PERFORMING_PH' in row):
                med_name = row.strip().split(" ")[1]
                med_name = med_name[1:]
                med_lastname = row.strip().split(" ")[2]
                med_lastname = med_lastname[:-1]
            elif ('PATNAME' in row):
                pat_fullname = row.strip().split(" ")[1]
                pat_fullname = row.strip().split(", ")
                pat_name = pat_fullname[1][:-1]
                pat_lastname = pat_fullname[0].split(" ")[1][1:]
            elif ('PATID' in row):
                pat_id = row.strip().split(" ")[1]
                pat_id = pat_id[1:]
                pat_id = pat_id[:-1]
            elif ('GESTATIONS' in row):
                num_gesta = row.strip().split(" ")[1]
            elif ('CLINICAL_LMP' in row):
                lmp = row.strip().split(" ")[1]
            elif ('CLINICAL_GA' in row):
                clinical_ga = row.strip().split(" ")
                ga_weeks = clinical_ga[1][:-1]
                ga_days = clinical_ga[2][:-1]
                clinical_ga = ga_weeks+" "+ga_days
            elif ('CLINICAL_EDC' in row):
                CLINICAL_EDC = row.strip().split(" ")[1]
            elif ('EFW_HADLOCK' in row):
                EFW = row.strip().split(" ")[1] # Estimated Fetal Weight
            else:
                not_found_pacient = False
                            
        count += 1
        
        error = []
        if not_found_pacient == True:
            error.append('No se encontró información del paciente')
        else:
            if studydate and studytime:
                convertedDate = ConvertDateTime(studydate, studytime)
            else:
                # Handle the case when studydate or studytime is not defined or empty
                convertedDate = None  # Or any appropriate handling you prefer

            insert_paciente = {
            'cedulapac': pat_id,
            'apellido_paterno': pat_lastname,
            'nombreuno':pat_name,
            'numgestacion':num_gesta,
            'lmp': lmp
            }
        
        count = 0
        flag = False
        for row_bytes in file_readed:
            line = row_bytes.decode("utf-8") 
        # BIORBITAL DIAMETER Diámetro bi-orbitario externo
            if ('BEGIN FETALBIO' in line):
                flag = True
            if ('END FETALBIO' in line):
                False
                        
            if flag:
                if ('BOD_JEANTY' in line):
                    BOD_JEANTY = line.strip().split("|")
                    BOD_JEANTY = BOD_JEANTY[:-1]
                    BOD_JEANTY = BOD_JEANTY[0].split("=")[1].split(" ")[0] #1
                    BOD_JEANTY = (float(BOD_JEANTY)*10) #To mm
                # diámetro transverso del cerebelo
                if ('CEREB_HILL' in line):
                    CEREB_HILL = line.strip().split("|")
                    CEREB_HILL = CEREB_HILL[:-1]
                    cereb_hill_1 = CEREB_HILL[0].split("=")[1].split(" ")[0] #1
                    cereb_hill_1 = np.round((float(cereb_hill_1)*10), decimals=2) #To mm
                # BIPARIETAL DIAMETER Diametro Biparietal (Distancia en milímetros entre ambos huesos parietales de la cabeza del bebé)
                if ('BPD_HADLOCK' in line):
                    BPD_HADLOCK = line.strip().split("|")
                    BPD_HADLOCK = BPD_HADLOCK[:-1]
                    bpd_hadlock_1 = BPD_HADLOCK[0].split("=")[1].split(" ")[0] #1
                    bpd_hadlock_1 = np.round((float(bpd_hadlock_1)*10), decimals=2) #To mm
                # CISTERNA MAGNA
                if ('CM' in line):
                    CM = line.strip().split("|")
                    CM = CM[:-1]
                    cm_1 = CM[0].split("=")[1].split(" ")[0] #1
                # CAVUM SEPTI PELLUCIDI
                if ('CSP' in line):
                    CSP = line.strip().split("|")
                    CSP = CSP[:-1]
                    csp_1 = CSP[0].split("=")[1].split(" ")[0] #1
                # HEAD CIRCUMFERENCE
                if ('HC_HADLOCK' in line):
                    HC_HADLOCK = line.strip().split("|")
                    HC_HADLOCK = HC_HADLOCK[:-1]
                    hc_hadlock_1 = HC_HADLOCK[0].split("=")[1].split(" ")[0] #1
                    hc_hadlock_1 = np.round((float(hc_hadlock_1)*10), decimals=2) #To mm
                # Va Anterior Ventricle
                if ('Va' in line):
                    Va = line.strip().split("|")
                    Va = Va[:-1]
                    va_1= Va[0].split("=")[1].split(" ")[0] #1
                # Vp Posterior ventricle
                if ('Vp' in line):
                    Vp = line.strip().split("|")
                    Vp = Vp[:-1]
                    vp_1 = Vp[0].split("=")[1].split(" ")[0] #1
                if ('AFI' in line):
                    afi = line.strip().split("|")
                    afi = afi[:-1]
                    afi_sum = afi[4].split("=")[1].split(" ")[0]
            if line.startswith('COMMENT'):
                try:
                    text = re.search(r'"([^"]*)"', line).group(1)
                    comments = re.sub(r'\\n', ' - ', text)
                except:
                    comments = None
                
        reporte_info = {
            'efw': EFW,
            'edb': CLINICAL_EDC,
            'ga': ga_weeks,
            'csp_1': csp_1,
            'cm_1': cm_1,
            'hc_hadlock_1': hc_hadlock_1,
            'bpd_hadlock_1': bpd_hadlock_1,
            'cereb_hill_1': cereb_hill_1,
            'va_1': va_1,
            'vp_1': vp_1,
            'ga_days': ga_days,
            'afi': afi_sum
        }
        
        
        return insert_paciente, reporte_info, convertedDate, med_name, med_lastname, comments
    except Exception as e:
        # Handle the exception
        print(f"An error occurred: {e}")

    
def ConvertDateTime(studydate, studytime):
    if studydate is None or studytime is None:
        return None
    
    day = studydate.split(".")[0]
    month = studydate.split(".")[1]
    year = studydate.split(".")[2]
    
    fullDate = year+"-"+month+"-"+day+" "+studytime
    return fullDate

def comparison(diagnosisData):
    gest_age = diagnosisData['ga']
    
    data = {'hc_hadlock': diagnosisData['hc_hadlock_1'], 'bpd_hadlock': diagnosisData['bpd_hadlock_1'], 'csp': diagnosisData['csp_1'],
            'cm': diagnosisData['cm_1'], 'vp': diagnosisData['vp_1'], 'va': diagnosisData['va_1'], 'cereb_hill': diagnosisData['cereb_hill_1'],
            'efw': diagnosisData['efw'], 'afi': diagnosisData['afi']}
    diagnosisResult = {'hc_hadlock':'', 'bpd_hadlock': '', 'csp': '', 'cm':'', 'vp': '', 'va': '', 'cereb_hill':'', 'efw': '', 'afi': ''}

    tipos_mediciones = Tipomedicion.objects.all()
    mediciones = {}

    for obj in tipos_mediciones:
        mediciones[obj.idTipoMedicion] = obj.nombreMedicion

    for key in mediciones:
        if key == 1 or key == 2 or key == 7 or key == 3 or key==9:
            try:
                med = Medicion.objects.get(id_tipo_medicion=key, ga=gest_age)
                
                if key == 1: #HC_HADLOCK
                    if float(data["hc_hadlock"]) == 0:
                        diagnosisResult["hc_hadlock"] = 'None'
                        
                    elif (data["hc_hadlock"] > med.valorinter):
                        diagnosisResult["hc_hadlock"] = 'Macrocrania'
                        
                    elif (data["hc_hadlock"] < med.valormin):
                        diagnosisResult["hc_hadlock"] = 'Microcefalia'
                    else:
                        diagnosisResult["hc_hadlock"] = 'Normal'

                if key == 2: #BPD
                    if float(data["bpd_hadlock"]) == 0:
                        diagnosisResult["bpd_hadlock"] = 'None'
                    elif (data["bpd_hadlock"] > med.valorinter):
                        diagnosisResult["bpd_hadlock"] = 'Anormalidad por valor superior'
                        
                    elif (data["bpd_hadlock"] < med.valormin):
                        diagnosisResult["bpd_hadlock"] = 'Anormalidad por valor inferior'
                        
                    else:
                        diagnosisResult["bpd_hadlock"] = 'Normal'
                        
                if key == 7: #Diametro transverso del cerebelo CEREB_HILL
                    if float(data["cereb_hill"]) == 0:
                        diagnosisResult["cereb_hill"] = 'None'
                    elif (data["cereb_hill"] < med.valormin):
                        diagnosisResult["cereb_hill"] = 'Hipoplasia cereberal'
                    else:
                        diagnosisResult["cereb_hill"] = 'Normal'
                
                if key == 3: #CSP
                    if float(data["csp"]) == 0:
                        diagnosisResult["csp"] = 'None'
                    elif (float(data["csp"]) > med.valorinter):
                        diagnosisResult["csp"] = 'Anormalidad por valor superior'
                        
                    elif (float(data["csp"]) < med.valormin):
                        diagnosisResult["csp"] = 'Anormalidad por valor inferior'                            
                    else:
                        diagnosisResult["csp"] = 'Normal'
                        
                if key == 9: #EFW
                    if float(data["efw"]) == 0:
                        diagnosisResult["efw"] = 'None'
                    elif (float(data["efw"]) > med.valorinter):
                        diagnosisResult["efw"] = 'Feto grande para la edad gestacional'
                        
                    elif (float(data["efw"]) < med.valordev):
                        
                        if (float(data["efw"]) < med.valormin):
                            diagnosisResult["efw"] = 'R.C.I.U (Restricción del crecimiento interuterino)'
                        else:
                            diagnosisResult["efw"] = 'Feto pequeño para la edad gestacional' 
                    
                    elif ( med.valordev < float(data["efw"]) < med.valorinter):
                        diagnosisResult["efw"] = 'Normal'
        
            except Medicion.DoesNotExist:
                med = None
                print("Para la medición:", key, "no se encontró nada con esta edad gestacional")
                     
        if key == 4: #CM -> Para todas las edades
            if float(data["cm"]) == 0:
                diagnosisResult["cm"] = 'None'
            elif (float(data["cm"]) > settings.CM_REF):
                diagnosisResult["cm"] = 'Megacisterna o cisterno alargada'
            else:
                diagnosisResult["cm"] = 'Normal'
                    
        if key == 5: #VP or VA
            if float(data["vp"]) == 0:
                diagnosisResult["vp"] = 'None'
            elif (float(data["vp"]) < settings.VT_MIN):
                diagnosisResult["vp"] = 'Normal'

            elif ((settings.VT_1 < float(data["vp"]) < settings.VT_2) ):
                diagnosisResult["vp"] = 'Ventriculomegalia leve'

            elif (settings.VT_3 < float(data["vp"]) < settings.VT_4 ):
                diagnosisResult["vp"] = 'Ventriculomegalia moderada'
                
            elif (float(data["vp"]) > settings.VT_MAX ):
                diagnosisResult["vp"] = 'Ventriculomegalia severa'
        
        if key == 6: #VP or VA
            if float(data["va"])== 0:
                diagnosisResult["va"] = 'None'

            elif(float(data["va"]) < settings.VT_MIN):
                diagnosisResult["va"] = 'Normal'

            elif ( (settings.VT_1 < float(data["va"]) < settings.VT_2)):
                diagnosisResult["va"] = 'Ventriculomegalia leve'

            elif (settings.VT_3 < float(data["va"]) < settings.VT_4):
                diagnosisResult["va"] = 'Ventriculomegalia moderada'
                
            elif ( float(data["va"]) > settings.VT_MAX):
                diagnosisResult["va"] = 'Ventriculomegalia severa'
 
        if key == 8:
            if float(data["afi"]) == 0:
                diagnosisResult["afi"] = 'None'
            elif (float(data["afi"]) < settings.AFI_MIN):
                diagnosisResult["afi"] = 'Oligohidramnios'
                
            elif (settings.AFI_MIN < float(data["afi"]) < settings.AFI_MAX):
                diagnosisResult["afi"] = 'Normal'
                
            elif (float(data["afi"]) > settings.AFI_MAX):
                diagnosisResult["afi"] = 'Polihidramnios'
    return diagnosisResult
