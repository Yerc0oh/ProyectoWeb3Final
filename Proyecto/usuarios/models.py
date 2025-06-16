# Create your models here.
# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('administrador', 'Administrador'),
        ('usuarionormal', 'Usuario Normal'),
    )
    rol = models.CharField(max_length=30, choices=ROLES)
