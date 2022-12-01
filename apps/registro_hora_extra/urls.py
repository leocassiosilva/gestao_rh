from django.urls import path, include

from .views import ExportarParaCSV,ExportarExcel, HoraExtraList, HoraExtraDelete, HoraExtraCreate, HoraExtraUpdate, HoraExtraUpdateBase, UtilizouHoraExtra

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraUpdate.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraUpdateBase.as_view(), name='update_hora_extra_base'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('exportar-csv', ExportarParaCSV.as_view(), name='exportar_csv'),
    path('exportar-excel', ExportarExcel.as_view(), name='exportar_excel'),
]
