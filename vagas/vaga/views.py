from django.http import JsonResponse
from vagas.vaga.models import Vaga


def vaga(request, pk: int):
    vaga = Vaga.objects.get(id=pk)
    return JsonResponse(vaga.vaga_to_dict(), json_dumps_params={"ensure_ascii": False})


def vagas(request):
    vagas = Vaga.objects.all()
    vagas_dict = {}
    vagas_list = []
    for vaga in vagas:
        vagas_list.append(vaga.vaga_to_dict())
        vagas_dict.update({"vagas": vagas_list})
    return JsonResponse(vagas_dict, json_dumps_params={"ensure_ascii": False})
