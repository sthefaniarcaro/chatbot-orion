"""Teste de fumaça: a aplicação sobe e responde.

ARQUIVO DO PROFESSOR: não altere.
"""


def test_pagina_de_chat_responde(cliente):
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert "Assistente de dúvidas" in resposta.text


def test_rota_de_saude(cliente):
    resposta = cliente.get("/saude")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


def test_usa_o_banco_temporario(cliente, caminho_banco):
    # Os testes nunca usam o chatbot.db de verdade.
    assert cliente.app.state.caminho_banco == caminho_banco
