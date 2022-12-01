import json
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from apps.registro_hora_extra.forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra
from django.contrib.auth.models import User
from django.urls import reverse

class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraUpdate(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraUpdateBase(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario','horas']

    def get_success_url(self):
        return reverse('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraUpdateBase, self).get_form_kwargs()
        # kwargs.update({'user': self.request.user})
        return kwargs
class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        empregado = self.request.user.funcionario

        response = json.dumps(
            {'mensagem': 'Requisicao executada',
             'horas': float(empregado.total_horas_extra)
             }
        )

        return HttpResponse(response, content_type='application/json')


    
