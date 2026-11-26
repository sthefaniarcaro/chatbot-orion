"""Ponto de entrada do assistente de dúvidas.

Este é o esqueleto do projeto: só sobe a API e a página de chat.
As regras de negócio entram módulo a módulo, a partir da aula 6.

Para rodar:  py -m uvicorn app.main:app --reload
"""

import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

PASTA = Path(__file__).parent


def criar_app(caminho_banco: str | None = None) -> FastAPI:
    """Monta a aplicação.

    Recebe o caminho do banco SQLite em vez de fixá-lo no código: assim os
    testes passam um banco temporário e nunca tocam no banco de verdade.
    """
    app = FastAPI(title="Assistente de dúvidas")
    app.state.caminho_banco = caminho_banco or os.environ.get("CHATBOT_DB", "chatbot.db")

    @app.get("/", response_class=HTMLResponse)
    def pagina() -> str:
        return (PASTA / "pagina.html").read_text(encoding="utf-8")

    @app.get("/saude")
    def saude() -> dict:
        return {"status": "ok"}

    return app


app = criar_app()
