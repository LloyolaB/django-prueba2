from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("crear_reserva/", crear_reserva, name="crear_reserva"),
    path("listar_reserva/", listar_reservas, name="listar_reserva"),
    path("editar_reserva/<int:id>", editar_reserva, name="editar_reserva"),
    path("eliminar_reserva/<int:id>", eliminar_reserva, name="eliminar_reserva"),
]
