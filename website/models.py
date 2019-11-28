from django.db import models

# Create your models here.

class Carro(models.Model):
    nome = models.CharField(max_length=50, default='')
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=30)

    def __str__(self):
        return self.nome