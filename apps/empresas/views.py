from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import Empresa

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']
    template_name = 'empresas/empresa_form.html'

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse("ok")


class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['nome']