from django.db import models

# Create your models here.

class Carro(models.Model):
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=30)

def __str__(self):
    return self.placa