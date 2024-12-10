from django.db import models

# Create your models here.
class Futbol(models.Model):    
    equipo = models.CharField(max_length=40)
    talle = models.IntegerField()
    numero = models.IntegerField()
    def __str__(self):
        return f"Equipo: {self.equipo} Talle: {self.talle} Numero: {self.numero}"

class Basquet(models.Model):    
    equipo = models.CharField(max_length=40)
    talle = models.IntegerField()
    numero = models.IntegerField()
    def __str__(self):
        return f"Equipo: {self.equipo} Talle: {self.talle} Numero: {self.numero}"

class Rugby(models.Model):    
    equipo = models.CharField(max_length=40)
    talle = models.IntegerField()
    numero = models.IntegerField()
    def __str__(self):
        return f"Equipo: {self.equipo} Talle: {self.talle} Numero: {self.numero}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()


