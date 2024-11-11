import pytest
from app.models import Equipamento
from app.utils import obter_data_do_proximo_ano
from app.utils.enums import CategoriaEPI


@pytest.mark.django_db()
def test_criacao_equipamento(equipamento_para_testes: Equipamento) -> None:
    # Testa a criação de uma instância de Equipamento
    equipamento = equipamento_para_testes

    assert equipamento.nome == "Luvas de Proteção"
    assert equipamento.categoria == CategoriaEPI.PROTECAO_MAOS_E_BRACOS
    assert equipamento.quantidade_total == 25
    assert equipamento.validade == obter_data_do_proximo_ano()
