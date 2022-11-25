from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Documento
from django.contrib.auth.models import User

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
