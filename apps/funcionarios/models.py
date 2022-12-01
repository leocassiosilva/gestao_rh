from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from apps.empresas.models import Empresa
from apps.departamentos.models import Departamento
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse_lazy('list_funcionario')

    @property
    def total_horas_extra(self):
        total = self.registrohoraextra_set.filter(utilizada=False).aggregate(
            Sum('horas'))['horas__sum']
        return total or 0

    def __str__(self):
        return self.nome
