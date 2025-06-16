from django import forms
from .models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'apellido', 'email', 'telefono', 'id_especialidad']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'direccion']

class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['id_doctor', 'dia_semana', 'hora_inicio', 'hora_fin']
class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['id_doctor', 'id_paciente', 'fecha_hora', 'motivo_consulta', 'recordatorio_enviado','fecha_recordatorio']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_recordatorio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion']
