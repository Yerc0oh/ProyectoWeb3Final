from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_disponibilidad/', views.crear_disponibilidad, name='crear_disponibilidad'),
    path('ver_disponibilidad/', views.ver_disponibilidad, name='ver_disponibilidad'),
    path('editar/<int:id_disponibilidad>/', views.editar_disponibilidad, name='editar_disponibilidad'),
    path('borrar/<int:id_disponibilidad>/', views.borrar_disponibilidad, name='borrar_disponibilidad'),
]
