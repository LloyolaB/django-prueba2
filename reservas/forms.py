from django import forms
from .models import Reserva


class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        exclude = ["creado_en", "actualizado_en"]
        fields = "__all__"


class FormActualizarReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        exclude = ["creado_en", "actualizado_en"]
        fields = "__all__"
