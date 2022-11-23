from django.urls import path, include

from .views import DepartamentoList, DepartamentoCreate

urlpatterns = [
    path('', DepartamentoList.as_view(), name='list_departamentos'),
    path('criar/', DepartamentoCreate.as_view(), name='create_departamento'),
    # path('editar/<int:pk>/', EmpresaUpdate.as_view(), name='edit_empresa'),
]
