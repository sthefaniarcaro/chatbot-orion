# Assistente de dúvidas — chatbot-[grupo]

Projeto e Implementação de Sistemas · Unesp

Chatbot que responde perguntas sobre os documentos do tema do grupo, citando
as fontes. Construído um módulo por aula, a partir da aula 6.

## Começar

```
py -m venv .venv --prompt chatbot
.venv\Scripts\activate
py -m pip install -r requirements.txt
py -m pytest
py -m uvicorn app.main:app --reload
```

Abra http://127.0.0.1:8000 (página de chat) e http://127.0.0.1:8000/docs (API).

Se o PowerShell bloquear o `activate`:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.

## Pastas

| Pasta | O que tem | Quem mexe |
|---|---|---|
| `app/` | Código da aplicação | O grupo (com o copiloto) |
| `tests/conftest.py`, `tests/test_sobe.py` | Fixtures e teste de fumaça | **Professor: não altere** |
| `tests/modulos/` | Testes de cada módulo | **Professor: não altere** |
| `tests/grupo/` | Testes do grupo | O grupo |
| `docs/modelo/` | Diagramas UML (.drawio e .png) | O grupo |
| `docs/fontes/` | Documentos do tema | O grupo |
| `docs/requisitos.md` | Lista oficial de requisitos | Professor (cópia) |

## Regras

1. Diagramas sem IA.
2. O copiloto recebe o diagrama e os testes do módulo como contexto.
3. Os testes do professor não mudam.
4. Todo pull request fecha uma história (`Fecha #N`) e é revisado por outro integrante.

Segredos (senhas, chaves) só no `.env`, que não vai para o Git. Modelo: `.env.exemplo`.
