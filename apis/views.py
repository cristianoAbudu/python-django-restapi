from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

from rest_framework import generics

class ColaboradorViewSet(viewsets.ModelViewSet):
	queryset = ColaboradorModel.objects.all()
	serializer_class = ColaboradorSerializer
