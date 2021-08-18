from django.contrib import admin

from vagas.vaga.models import Vaga


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = (
        'disponivel',
        'nome',
        'empresa',
        'salario',
        'area',
        'linguagem',
        'framework',
        'created_at',
        'uploaded_at',
    )
