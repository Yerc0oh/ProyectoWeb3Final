from django.urls import path
<<<<<<< HEAD
from . import views

app_name = 'turnos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
=======
from . import views  # Asegúrate de que esto esté

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

    


>>>>>>> 5e2ec6d (se realiazo la creacion de los formularios de regsitro de medico y paciente con sus respectivos templates)
]
