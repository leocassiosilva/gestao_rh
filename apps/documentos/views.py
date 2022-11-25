from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Documento
from django.contrib.auth.models import User

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)