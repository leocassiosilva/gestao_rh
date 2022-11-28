from django.urls import path, include

from .views import HoraExtraList, HoraExtraDelete, HoraExtraCreate, HoraExtraUpdate, HoraExtraUpdateBase

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraUpdate.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraUpdateBase.as_view(), name='update_hora_extra_base'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
]
