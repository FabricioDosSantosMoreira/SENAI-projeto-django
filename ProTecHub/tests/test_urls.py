from django.urls import reverse
from django.test import Client


def test_home_url():
    assert reverse('home') == '/'


def test_home_ok():
    client = Client()
    response = client.get(reverse('home'))
    assert response.status_code == 200


def test_cadastro_url():
    assert reverse('cadastro') == '/cadastro/'


def test_cadastro_ok():
    client = Client()
    response = client.get(reverse('cadastro'))
    assert response.status_code == 200


def test_logout_url():
    assert reverse('logout') == '/logout/'


def test_logout_ok():
    client = Client()
    response = client.get(reverse('logout'))
    assert response.status_code == 200


def test_login_url():
    assert reverse('login') == '/login/'


def test_login_ok():
    client = Client()
    response = client.get(reverse('login'))
    assert response.status_code == 200
