from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('enviar-recordatorios/', views.recordatorio, name='enviar_recordatorios'),

]
