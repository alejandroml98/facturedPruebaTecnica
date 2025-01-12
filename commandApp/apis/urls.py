from django.urls import path

from . import tableros_views

urlpatterns = [
    #path("", views.index, name="index"),
    path("tablero", tableros_views.TablerosCreate.as_view(), name="tableros_create"),
    path("tablero/<int:pk>", tableros_views.TablerosModify.as_view(), name='tableros_modify'),
]