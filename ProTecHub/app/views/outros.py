from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def contato(request: WSGIRequest) -> HttpResponse:

    return render(request, 'pages/contato.html')


def sobre(request: WSGIRequest) -> HttpResponse:

    return render(request, 'pages/sobre.html')
