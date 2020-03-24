from django.db import models

# Create your models here.

class Usuario(models.Model):
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)

class Autenticavel(models.Model):
    key = models.CharField(max_length=50)
    nome = models.CharField(max_length=30)
