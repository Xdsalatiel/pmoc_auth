from django.db import models

class Equipamento(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    capacidade_btus = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=100)
    ultima_manutencao = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.marca}"
