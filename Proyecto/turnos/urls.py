from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
