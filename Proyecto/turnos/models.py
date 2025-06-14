from django.db import models

# Create your models here.

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    id_doctor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='doctores')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.id_especialidad.nombre}"
    
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Disponibilidad(models.Model):
    id_disponibilidad = models.AutoField(primary_key=True)
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='disponibilidades')
    dia_semana = models.CharField(max_length=10, choices=[
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    )
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.id_doctor.nombre} {self.id_doctor.apellido} - {self.dia_semana} {self.hora_inicio}-{self.hora_fin}"
    
class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    id_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='turnos')
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='turnos')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    motivo_consulta = models.TextField(blank=True, null=True)
    recordatorio_enviado = models.BooleanField(default=False)
    fecha_recordatorio = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Turno: {self.id_turno} - {self.id_doctor.nombre} {self.id_doctor.apellido} - {self.fecha_hora.strftime('%Y-%m-%d %H:%M')} - {self.id_paciente.nombre} {self.id_paciente.apellido}"
    
