from django.db import models

class Alumno(models.Model):
    numControl = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=50)
    primerAP = models.CharField(max_length=50)
    segundoAP = models.CharField(max_length=50)
    fechaNac = models.DateField()
    semestre = models.IntegerField()
    carrera = models.CharField(max_length=50)

    class Meta:          
        db_table = 'alumnos'