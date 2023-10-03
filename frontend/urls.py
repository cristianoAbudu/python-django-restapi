from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("salvarColaborador/", views.get_name, name="salvarColaborador"),

]