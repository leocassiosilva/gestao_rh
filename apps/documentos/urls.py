from django.urls import path, include
from .views import (DocumentoCreate)

urlpatterns = [
    path('novo', DocumentoCreate.as_view(), name='create_documento'),
    # path('editar/<int:pk>/', FuncionariosUpdate.as_view(), name='update_funcionario'),
    # path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionario'),
    # path('criar/', FuncionariosCreate.as_view(), name='create_funcionario'),

]
