# Create your models here.
# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('doctor', 'Doctor'),
        ('paciente', 'Paciente'),
    )
    rol = models.CharField(max_length=10, choices=ROLES)
