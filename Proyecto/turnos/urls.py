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

    
    path('recordatorio/', views.recordatorio, name='recordatorio'),
    path('', views.inicio, name='inicio'),

    path('crear_disponibilidad/', views.crear_disponibilidad, name='crear_disponibilidad'),
    path('ver_disponibilidad/', views.ver_disponibilidad, name='ver_disponibilidad'),
    path('editar/<int:id_disponibilidad>/', views.editar_disponibilidad, name='editar_disponibilidad'),
    path('borrar/<int:id_disponibilidad>/', views.borrar_disponibilidad, name='borrar_disponibilidad'),

    path('lista_turnos/', views.lista_turnos, name='lista_turnos'),
    path('registrar_turno/', views.registrar_turno, name='registrar_turno'),
    path('turnos/editar/<int:id_turno>/', views.editar_turno, name='editar_turno'),
    path('turnos/eliminar/<int:id_turno>/', views.eliminar_turno, name='eliminar_turno'),
    path('registrar_especialidad/', views.registrar_especialidad, name='registrar_especialidad'),
    path('especialidades/', views.lista_especialidades, name='lista_especialidades'),
    path('especialidades/editar/<int:id_especialidad>/', views.editar_especialidad, name='editar_especialidad'),
    path('especialidades/eliminar/<int:id_especialidad>/', views.eliminar_especialidad, name='eliminar_especialidad'),

]
