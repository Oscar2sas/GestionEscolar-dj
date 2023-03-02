from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombreUsuarios = models.TextField(max_length=50)
    correoUsuarios = models.EmailField()
    passwordUsuarios = models.TextField(max_length=10)