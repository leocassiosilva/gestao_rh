from django.urls import path, include

from .views import EmpresaCreate, EmpresaUpdate

urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', EmpresaUpdate.as_view(), name='edit_empresa'),
]
