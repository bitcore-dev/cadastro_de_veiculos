from django.contrib import admin
from .models import Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):

    list_display = (
        'tipo',
        'marca',
        'modelo',
        'placa',
        'ano',
        'combustivel',
        'quilometragem',
    )

    list_filter = (
        'tipo',
        'marca',
        'combustivel',
    )

    search_fields = (
        'placa',
        'modelo',
        'marca',
    )