from typing import List

import pytest
from app.models import Equipamento, Usuario
from app.utils import (
    obter_data_atual, 
    obter_data_do_proximo_ano,  
    obter_data_do_proximo_mes
)
from app.utils.enums import Cargos, CategoriaEPI, TipoUsuario


@pytest.fixture
def equipamento_para_testes(db) -> Equipamento:
    return Equipamento.objects.create(
        nome="Luvas de Proteção",
        categoria=CategoriaEPI.PROTECAO_MAOS_E_BRACOS,
        quantidade_total=25,
        validade=obter_data_do_proximo_ano(), 
    )


@pytest.fixture
def equipamentos_para_testes(db) -> List[Equipamento]:
    return [
        Equipamento.objects.create(
            nome="Luvas de Proteção",
            categoria=CategoriaEPI.PROTECAO_MAOS_E_BRACOS,
            quantidade_total=25,
            validade=obter_data_do_proximo_ano(),
        ),
        Equipamento.objects.create(
            nome="Óculos de Proteção",
            categoria=CategoriaEPI.PROTECAO_OCULAR_E_FACIAL,
            quantidade_total=100,
            validade=obter_data_do_proximo_mes(),
        )
    ]


@pytest.fixture
def criar_usuario_administrador(db) -> Usuario:
    return Usuario.objects.create_user(
        nome="Admin", 
        email="Admin@test.com",
        username="Admin@test.com",
        password="pbkdf2_sha256$870000$msPKoTTGCXKpkI8n62hPL1$WHF8h4UtRTg5hJ9xakoNcU5n7lnOIxcnTQqcK6kflIE=",
        cargo=Cargos.TI,
        tipo=TipoUsuario.ADMINISTRADOR,
        foto=None,
        data_admissao=obter_data_atual
    )
   