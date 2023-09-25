from django.contrib import admin
from .models import Hospital, Images, Personalsalud, Consulta
# Register your models here.
class PersonalAdmin(admin.ModelAdmin) :
    fieldsets = [
            ("Header", {"fields": ['cedulamed']}),
            ("Content", {"fields": [ 'nombresmed', 'apellidosmed', 'telefonomed', 'direccionmed', 'hospitalid']}),
    ]

class HospitalAdmin(admin.ModelAdmin) :
    fieldsets = [
        ("Header", {"fields": ['nombrehospital']}),
        ("Content", {"fields": ['ciudad', 'departamento']}),
    ]

class ConsultaAdmin(admin.ModelAdmin) :
    fieldsets = [
            ("Content", {"fields": [ 'motivo_consulta', 'txtresults', 'medConsulta', 'medUltrasonido', 'idfeto']}),
            ("Date", {"fields": ['fecha_consulta']})
    ]
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Personalsalud,PersonalAdmin)
admin.site.register(Consulta,ConsultaAdmin)
admin.site.register(Images)


