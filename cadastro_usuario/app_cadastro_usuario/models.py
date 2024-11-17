from django.db import models

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome  = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    cpf = models.TextField(max_length=14)
    dt_nasc = models.DateField()
