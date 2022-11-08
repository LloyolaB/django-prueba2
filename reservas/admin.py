from django.contrib import admin
from .models import Reserva

# Register your models here.


@admin.register(Reserva)
class ReservasAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha", "hora", "telefono", "estado", "qty_personas"]
    list_filter = ["fecha", "estado"]
    search_fields = ["nombre", "fecha", "hora", "telefono", "estado", "qty_personas"]
    list_per_page = 10
