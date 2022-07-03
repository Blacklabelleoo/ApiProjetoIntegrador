from ast import Delete
from tkinter import CASCADE
from django.db import models

class Sobra(models.Model):
    comprimento = models.FloatField()
    largura     = models.FloatField()
    material    = models.CharField(max_length=20)

    def __str__(self):
        return self.material

class Peca(models.Model):
    comprimento = models.FloatField()
    largura     = models.FloatField()
    material    = models.CharField(max_length=20)

    def __str__(self):
        return self.material

class Aproveita(models.Model):
    sobra = models.ForeignKey(Sobra, on_delete = models.CASCADE)  
    peca = models.ForeignKey(Peca, on_delete = models.CASCADE) 