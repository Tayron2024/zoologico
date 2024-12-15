from logging import setLoggerClass
from time import sleep

from django.db import models
from django.db.models.fields import return_None


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class RegistroMedico(models.Model):
    Id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateField()
    diagnostico = models.CharField(max_length=100)
    peso = models.FloatField()
    tratamiento = models.CharField(max_length=100)
    vacunaAplicada = models.CharField(max_length=100)
    observacion = models.CharField(max_length=100)

    def __str__(self):
        return self.diagnostico + ' ' + self.tratamiento + ' ' + self.vacunaAplicada + ' ' + self.observacion

class Animal(models.Model):
    idAnimal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    genero = models.CharField(max_length=20)
    edad = models.IntegerField()

    def __str__(self):
        return self.idAnimal + ' ' +  self.edad

class Cliente(Persona):
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    socio = models.BooleanField(default=False)

class Visitante(Persona):
    discapacidad = models.BooleanField(default=False)
    carnetEspecial = models.CharField(max_length=50)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    horarioTrabajo = models.TimeField()
    salarioZonaDeTrabajo = models.FloatField()

class Veterinario(Empleado):
    especialidad = models.CharField(max_length=100)
    titulacion = models.CharField(max_length=100)
    tratamientosAplicados = models.TextField()
    horariosTrabajo = models.TimeField()
    calcularCapacidadAtencion = models.FloatField()

class EncargadoLimpieza(Empleado):
    zona = models.CharField(max_length=100)
    herramientas = models.TextField()

class Inventario(models.Model):
    idInventario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    costo = models.FloatField()
    fechaCaducidad = models.DateField()

class Comprobante(models.Model):
    idFactura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    rfc = models.CharField(max_length=50)
    cantidadTotal = models.FloatField()
    tipoPago = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calcularTotalPago = models.FloatField()

class Zoologico(models.Model):
    nombre = models.CharField(max_length=100)
    tamanioZoologico = models.FloatField()
    calcularCapacidad = models.FloatField()

class Habitat(models.Model):
    tipo = models.CharField(max_length=100)
    temperatura = models.FloatField()
    humedad = models.FloatField()
    registrarCondicionesAmbientales = models.TextField()

class GuiaTuristico(Empleado):
    horario = models.TimeField()
    idioma = models.CharField(max_length=50)
    realizarTour = models.TextField()

class HistorialAlimentacion(models.Model):
    horario = models.TimeField()
    alimentos = models.CharField(max_length=100)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

