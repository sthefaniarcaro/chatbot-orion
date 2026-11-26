"""Peças compartilhadas pelos testes (fixtures).

ARQUIVO DO PROFESSOR: não altere. Ele pode ganhar fixtures novas junto com
os testes de cada módulo.

Qualquer teste pode pedir uma fixture pelo nome, como parâmetro:

    def test_algo(cliente):
        resposta = cliente.get("/")
"""

import pytest
from fastapi.testclient import TestClient

from app.main import criar_app


@pytest.fixture
def caminho_banco(tmp_path):
    """Caminho de um banco SQLite novo e vazio, apagado depois do teste."""
    return str(tmp_path / "teste.db")


@pytest.fixture
def cliente(caminho_banco):
    """Cliente HTTP falando com a aplicação, ligada ao banco temporário."""
    with TestClient(criar_app(caminho_banco=caminho_banco)) as c:
        yield c


class LLMFalsa:
    """Dublê da LLM: devolve sempre o mesmo texto e anota cada chamada.

    Nos testes, nunca se chama a LLM de verdade: a resposta muda a cada
    chamada e gasta cota. A interface definitiva entra na aula 10.
    """

    def __init__(self, resposta: str = "Resposta de teste."):
        self.resposta = resposta
        self.chamadas: list[str] = []

    def gerar(self, prompt: str) -> str:
        self.chamadas.append(prompt)
        return self.resposta


@pytest.fixture
def llm_falsa():
    """Uma LLMFalsa nova para cada teste."""
    return LLMFalsa()
