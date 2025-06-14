from django.contrib import admin
from .models import Especialidad, Doctor, Paciente, Disponibilidad, Turno
# Register your models here.
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id_especialidad', 'nombre', 'descripcion')
    search_fields = ('nombre',)
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id_doctor', 'nombre', 'apellido', 'email', 'telefono', 'id_especialidad')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('id_especialidad',)
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'direccion')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('fecha_nacimiento',)
@admin.register(Disponibilidad)
class DisponibilidadAdmin(admin.ModelAdmin):
    list_display = ('id_disponibilidad', 'id_doctor', 'dia_semana', 'hora_inicio', 'hora_fin')
    search_fields = ('id_doctor__nombre', 'id_doctor__apellido', 'dia_semana')
    list_filter = ('dia_semana', 'id_doctor')
@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('id_turno', 'id_doctor', 'id_paciente', 'fecha_hora', 'motivo_consulta')
    search_fields = ('id_doctor__nombre', 'id_doctor__apellido', 'id_paciente__nombre', 'id_paciente__apellido')
    list_filter = ('fecha_hora', 'id_doctor', 'id_paciente')
    