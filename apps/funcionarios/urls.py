from django.urls import path, include
from .views import FuncionariosList

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionario'),
]
