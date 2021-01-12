from django.db import models

class Pessoa(models.Model):
    nome = models.CharField()
    
class Aluno(models.Model):
    nome = models.CharField()
