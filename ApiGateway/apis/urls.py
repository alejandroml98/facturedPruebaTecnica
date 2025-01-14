from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    #URL tableros
    path("", views.Prueba.as_view(), name="prueba"),
]