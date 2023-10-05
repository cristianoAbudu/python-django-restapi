from django.shortcuts import render
from apis.models import ColaboradorModel
from django.http import HttpResponseRedirect

from .forms import AssociaChefeForm, ColaboradorForm

def index(request):
    colaborador_list = ColaboradorModel.objects.order_by("nome")
    form = ColaboradorForm()
    context = {
        "colaborador_list": colaborador_list,
        "form": form,
    }
    return render(request, "frontend/index.html", context)
#https://docs.djangoproject.com/en/4.2/topics/forms/
def get_name(request):
    if request.method == "POST":
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            model = ColaboradorModel()
            model.nome = form.cleaned_data['nome']
            model.senha = form.cleaned_data['senha']
            model.save()
    else:   
        form = ColaboradorForm()
    colaborador_list = ColaboradorModel.objects.order_by("nome")
    context = {"colaborador_list": colaborador_list}
    return index(request)

def associaChefe(request):
    if request.method == "POST":
        form = AssociaChefeForm(request.POST)
        if form.is_valid():

            chefe = ColaboradorModel.objects.get(id=form.data['chefe'])
            subordinado = ColaboradorModel.objects.get(id=form.data['subordinado'])

            if(chefe.id != subordinado.id) :
                subordinado.id_chefe = chefe.id
                subordinado.save()
            
    else:   
        form = ColaboradorForm()
    colaborador_list = ColaboradorModel.objects.order_by("nome")
    context = {"colaborador_list": colaborador_list}
    return index(request)