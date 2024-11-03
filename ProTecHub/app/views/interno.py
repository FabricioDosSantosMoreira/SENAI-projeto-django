from typing import Any, Dict

from app.models import Usuario

from .base import logar

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render

@login_required()
def interno(request: WSGIRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        messages.error(request, 'Você não está logado!')
        return redirect(logar)
    
    user_groups = request.user.groups.values_list('name', flat=True)
    foto = Usuario.objects.filter(id=request.user.pk).values_list('foto', flat=True).first()

    context: Dict[str, Any] = {
        'user_groups': user_groups,
        'foto': foto,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'pages/interno/home.html', context)
