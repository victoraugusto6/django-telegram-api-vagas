import pytest
from django.urls import reverse
from model_mommy import mommy

from django_assertions import assert_contains
from vagas.vaga.models import Vaga


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


@pytest.fixture
def vagas(db):
    return mommy.make(Vaga, 3)


def test_status_code(resp):
    assert resp.status_code == 200


def test_navbar_home_link(resp):
    assert_contains(resp, reverse('base:home'))


def test_navbar_api_link(resp):
    assert_contains(resp, reverse('vaga:vagas'))


def test_navbar_bot_link(resp):
    assert_contains(resp, 'href="https://t.me/django_telegram_api_bot"')


def test_navbar_admin_link(resp):
    assert_contains(resp, '/admin')


def vagas_no_template(resp, vagas):
    for vaga in vagas:
        assert_contains(resp, vaga.nome)
