from django.shortcuts import render
from rest_framework import generics
from .models import (
    Roles,
    UserRoles,
)
from .serializers import (
    RolesSerializer,
    UserSerializer,
    UserRolesSerializer,
)
from django.contrib.auth.models import User

class RolesView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class ManageRolesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRolesView(generics.ListCreateAPIView):
    queryset = UserRoles.objects.all()
    serializer_class = UserRolesSerializer  