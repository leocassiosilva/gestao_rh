from django.urls import path, include

from apps.core.views import home

urlpatterns = [
    path('', home, name='home'),
]
