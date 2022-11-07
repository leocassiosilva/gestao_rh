from django.db import models

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)