from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

from rest_framework import generics

from django.shortcuts import render
from django.views import View

class ColaboradorViewSet(viewsets.ModelViewSet):
	queryset = ColaboradorModel.objects.all()
	serializer_class = ColaboradorSerializer

def index(request):
    colaborador_list = ColaboradorModel.objects.order_by("nome")
    context = {"colaborador_list": colaborador_list}
    return render(request, "apis/index.html", context)


def get(self, request):
    return render(request, self.template)
    
def detail(request, question_id):
    return HTTPResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HTTPResponse(response % question_id)


def vote(request, question_id):
    return HTTPResponse("You're voting on question %s." % question_id)