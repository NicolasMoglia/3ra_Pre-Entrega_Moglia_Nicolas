from django.urls import path
from App1.views import futbol, basquet, inicio, formulario_futbol, formulario_basquet, rugby, formulario_rugby

urlpatterns = [
    path("futbol/",futbol, name="futbol"),
    path("basquet/",basquet, name="basquet"),
    path("rugby/",rugby, name="rugby"),
    path("",inicio, name=""),

    path("formulario_futbol/", formulario_futbol, name="formulario_futbol"),
    path("formulario_basquet/", formulario_basquet, name="formulario_basquet"),
    path("formulario_rugby/", formulario_rugby, name="formulario_rugby")
]