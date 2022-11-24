from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Departamento
from django.contrib.auth.models import User
# Create your views here.

class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Departamento.objects.filter(empresa=empresa_logada)
        return queryset

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    # def get_absolute_url(self):
    #     return reverse('list_departamentos')

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)

class DepartamentoUpdate(UpdateView):
    model  = Departamento
    fields = ['nome']  
    
    def get_success_url(self):
        return reverse('list_departamentos')

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')

