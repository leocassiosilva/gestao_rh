from django.urls import path, include
from .views import FuncionariosList, FuncionariosUpdate

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionario'),
    path('editar/<int:pk>/', FuncionariosUpdate.as_view(), name='update_funcionario'),

]
