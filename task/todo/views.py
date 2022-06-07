from django.shortcuts import render
from rest_framework import viewsets
from.models import Task
from .serializers import TaskSerializer
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly



# Create your views here.
class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
