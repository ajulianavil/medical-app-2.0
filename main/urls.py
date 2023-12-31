from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("landing", views.landing, name="landing"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
    path("howToRegister", views.howToRegister, name="howToRegister"),
    path("repositorio", views.repositorio, name="repositorio") ,
    path("historia_clinica", views.historia_clinica, name="historia_clinica"),
    path("registros/consulta", views.reportes, name="registros"),
    path("registros/consulta/<int:param>", views.reporteInfo, name="registroinfo"),
    path("usuario/nuevo", views.agregar_usuario, name="usuario/nuevo"),
    path("registros", views.reportes, name="registros"),
    path("reporte_pdf/<int:consultaid>/<int:reporteid>", views.reporte_pdf, name="reporte_pdf"),
    path("reporte/graficos/<int:consultaid>/<int:idreporte>", views.reporte_graficos, name="reporte_graficos"),
    path('chart-data/<int:idpaciente>/<int:idreporte_id>/<str:nombreMedicion>/<str:ga>/<int:consultaid>', views.chart_data_view, name='chart_data'),
    path("editPacientData/<int:consultaid>", views.editPacientData, name="editPacientData"),
    path("editReportData/<int:idreporte>", views.editReportData, name="editReportData"),
    path("usuario/listado", views.ver_usuarios, name="usuario/listado"),
    path("deactivateUser/<str:userid>", views.deactivateUser, name="deactivateUser"),
    path("reactivateUser/<str:userid>", views.reactivateUser, name="reactivateUser"),
    path("reporte/paciente_existe/<int:idpac>/<int:consultaid>", views.paciente_existe, name="paciente_existe"),
    path("consultas/historial/<int:idpac>", views.historial_paciente, name="historial_paciente"),
    path("consultas/resumen/<int:id_embarazo>", views.resumen_embarazo, name="resumen_embarazo"),
    path("consultas/nueva", views.temporal_embarazo, name="consultas/nueva"),
    path("consultas/nueva/unico", views.agregar_consulta, name="consultas/nueva/unico"),
    path("consultas/nueva/multiple", views.agregar_consulta_multiple, name="consultas/nueva/multiple"),
    path("reportes/temporal/multiple", views.temporal_historial, name="temporal_historial"),
    path("consultas/imagenes", views.upload_images, name="upload_images"),
    path("consultas/display_image/<int:reporte>", views.display_image, name="display_image"),
    path("institucion/nuevo", views.agregar_hospital, name="institucion/nuevo"),
]