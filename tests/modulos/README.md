# Testes dos módulos (do professor)

A cada aula, depois da modelagem, o professor publica os testes do módulo.
Copie a pasta da aula para cá, sem mudar nada:

```
tests/modulos/aula06_ingestao/
tests/modulos/aula07_arquitetura/
...
```

Estes testes são o critério de aceitação das histórias: a história está pronta
quando os testes do módulo passam.

**Não altere nada nesta pasta.** Na aula 6, quem revisa o pull request confere
com `git diff --stat main -- tests/modulos tests/conftest.py tests/test_sobe.py`.
A partir da aula 7, o CI confere automaticamente.
