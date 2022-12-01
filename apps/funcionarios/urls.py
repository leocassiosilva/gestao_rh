from django.urls import path, include
from .views import (FuncionariosDelete, FuncionariosList, FuncionariosUpdate, FuncionariosCreate, Pdf, PdfDebug,relatorio_funcionarios)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionario'),
    path('editar/<int:pk>/', FuncionariosUpdate.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionario'),
    path('criar/', FuncionariosCreate.as_view(), name='create_funcionario'),
    path('pdf-reportlab/', relatorio_funcionarios, name='pdf_reportlab'),
    path('relatorio_funcionarios_html', Pdf.as_view(), name='relatorio_funcionarios_html'),
    path('relatorio_funcionarios_html_debug', PdfDebug.as_view(), name='relatorio_funcionarios_html_debug'),


]
