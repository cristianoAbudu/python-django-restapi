from django.shortcuts import render
from apis.models import ColaboradorModel
from django.http import HttpResponseRedirect

from .forms import ColaboradorForm

def index(request):
    colaborador_list = ColaboradorModel.objects.order_by("nome")
    context = {"colaborador_list": colaborador_list}
    return render(request, "frontend/index.html", context)
#https://docs.djangoproject.com/en/4.2/topics/forms/
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ColaboradorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ColaboradorForm()

    return render(request, "name.html", {"form": form})
