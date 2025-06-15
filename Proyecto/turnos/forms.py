from django import forms
from .models import Doctor, Paciente

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'apellido', 'email', 'telefono', 'id_especialidad']

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'direccion']
