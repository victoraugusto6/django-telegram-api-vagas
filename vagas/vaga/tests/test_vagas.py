import pytest
from django.urls import reverse
from model_mommy import mommy

from django_assertions import assert_contains
from vagas.vaga.models import Vaga


@pytest.fixture
def resp(client, vagas, db):
    resp = client.get(reverse('vaga:vagas'))
    return resp


@pytest.fixture
def vagas(db):
    return mommy.make(Vaga, 2)


def test_vagas_status_code(resp):
    assert resp.status_code == 200


def test_nome_vagas(resp, vagas):
    for vaga in vagas:
        assert_contains(resp, vaga.nome)
