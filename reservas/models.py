from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Reserva(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre del cliente")
    fecha = models.DateField(verbose_name="Fecha de la reserva")
    hora = models.TimeField(verbose_name="Hora de la reserva")
    telefono = models.CharField(max_length=9, verbose_name="Telefono del cliente")
    # COMENZAMOS EL CHOICE
    ESTADO_CHOICES = (
        ("R", "RESERVADO"),
        ("C", "COMPLETADA"),
        ("A", "ANULADA"),
        ("N", "NO ASISTEN"),
    )
    estado = models.CharField(
        verbose_name="Estado de la reserva",
        max_length=20,
        choices=ESTADO_CHOICES,
        default="R",
    )

    qty_personas = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        default=1,
        verbose_name="Cantidad de personas",
    )
    comentario = models.TextField(verbose_name="Observación", blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
