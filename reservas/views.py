from django.shortcuts import render
from .models import Reserva
from .forms import FormReserva, FormActualizarReserva

# Create your views here.


def index(request):
    return render(request, "index.html")


def crear_reserva(request):
    form = FormReserva()
    if request.method == "POST":
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {"form": form}
    return render(request, "crear_reserva.html", data)


def listar_reservas(request):
    reserva = Reserva.objects.all()
    data = {"reserva": reserva}
    return render(request, "listar_reserva.html", data)


def editar_reserva(request, id):
    queryset = Reserva.objects.get(id=id)
    form = FormActualizarReserva(instance=queryset)
    if request.method == "POST":
        form = FormActualizarReserva(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
        return index(request)
    data = {"form": form}
    return render(request, "listar_reservas.html", data)


def eliminar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return listar_reservas(request)
