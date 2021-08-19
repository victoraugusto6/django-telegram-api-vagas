from django.shortcuts import render

from vagas.vaga.models import Vaga


def home(request):
    vagas = Vaga.objects.all()
    context = {
        'vagas': vagas
    }
    return render(request, 'base/home.html', context)
