from django.db import models

class Habitat(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Especie(models.Model):
    nombre_cientifico = models.CharField(max_length=100)
    nombre_comun = models.CharField(max_length=100)
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE, related_name='especies')

    def __str__(self):
        return f"{self.nombre_comun} ({self.nombre_cientifico})"

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='animales')
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre
from django.db import models

class Habitat(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'zoo'
