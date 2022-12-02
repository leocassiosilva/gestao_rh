from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.core.serializers import GroupSerializer, UserSerializer
from apps.funcionarios.models import Funcionario
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer