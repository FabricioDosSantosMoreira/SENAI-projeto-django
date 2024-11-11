from typing import List

import pytest
from app.models import Equipamento, Usuario
from django.test.client import Client
from django.urls import reverse


@pytest.mark.django_db()
def test_obter_equipamentos_view(
        client: Client, 
        criar_usuario_administrador: Usuario, 
        equipamentos_para_testes: List[Equipamento]
    ) -> None:

    # Autentica o usuário no client
    client.login(
        username="Admin@test.com", 
        password="pbkdf2_sha256$870000$msPKoTTGCXKpkI8n62hPL1$WHF8h4UtRTg5hJ9xakoNcU5n7lnOIxcnTQqcK6kflIE="
    )

    # Usa `reverse` para obter a URL da view
    url = reverse('obter_equipamentos') 
    response = client.get(url)

    # Verifica se o status da resposta é 200 (OK)
    assert response.status_code == 200

    assert "Luvas de Proteção" == response.context['equipamentos'][0].nome
    assert "Óculos de Proteção" == response.context['equipamentos'][1].nome

    assert equipamentos_para_testes[0] == response.context['equipamentos'][0]
    assert equipamentos_para_testes[1] == response.context['equipamentos'][1]
    assert len(response.context['equipamentos']) == 2
