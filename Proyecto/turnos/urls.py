from django.urls import path

from . import views

app_name = 'turnos'

urlpatterns = [
    # URLs para Doctores
    path('doctores/', views.lista_doctores, name='lista_doctores'),
    path('doctores/registrar/', views.registrar_doctor, name='registrar_doctor'),
    path('doctores/editar/<int:id_doctor>/', views.editar_doctor, name='editar_doctor'),
    path('doctores/eliminar/<int:id_doctor>/', views.eliminar_doctor, name='eliminar_doctor'),
    
    
    # URLs para Pacientes
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('pacientes/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/editar/<int:id_paciente>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id_paciente>/', views.eliminar_paciente, name='eliminar_paciente'),

    
    path('enviar-recordatorios/', views.recordatorio, name='enviar_recordatorios'),
    path('', views.inicio, name='inicio'),


]
