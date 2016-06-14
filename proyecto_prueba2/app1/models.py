from django.db import models



class Alumno(models.Model):
    nombre      = models.CharField(max_length=60)
    apellidos   = models.CharField(max_length=70)
    nif         = models.CharField(max_length=10)






