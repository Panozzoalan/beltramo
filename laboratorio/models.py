from django.db import models
from django.utils import timezone

class Paciente(models.Model):
   nombre_y_apellido = models.CharField(max_length=200)
   dni = models.IntegerField(max_length=8)
   telefono = models.CharField(max_length=20)
   fecha_nacimiento = models.DateTimeField()

   def __str__(self):
      return self.nombre_y_apellido


class Especialidad(models.Model):
   especializacion = models.CharField(max_length=200)

   def __str__(self):
      return self.especializacion


class Medico(models.Model):
   nombre_y_apellido = models.CharField(max_length=200)
   dni = models.IntegerField(max_length=8)
   telefono = models.CharField(max_length=20)
   especialidad = models.ForeignKey('Especialidad', on_delete=models.CASCADE)
   
   def __str__(self):
      return self.nombre_y_apellido   


class Estudio_medico(models.Model):
   paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
   medico = models.ManyToManyField('Medico')
   nombre = models.CharField(max_length=200)
   fecha = models.DateTimeField()

   def __str__(self):
      return self.nombre


