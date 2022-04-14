from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class TaskListViewSet(ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer