# Hands-On: Spec-Driven Development com GitHub Copilot

Este repositório entrega um hands-on simples e demonstrável de SDD com GitHub Copilot usando uma API de tarefas em FastAPI.

## O que este projeto mostra

- como sair de requisitos para design
- como transformar artefatos de especificacao em tarefas de implementacao
- como usar o Copilot para acelerar a construcao de uma API pequena
- como validar o resultado com um fluxo end-to-end executavel

## Formas de uso

### Demo rapida

Entre em hands-on e execute:

```bash
pip install -r requirements.txt
python demo_flow.py
```

### Workshop guiado

Entre em hands-on e siga esta ordem:

1. requirements.md
2. design.md
3. tasks.md
4. demo_flow.py para validacao final

Tempo estimado do workshop guiado: 25 a 30 minutos.

## Estrutura do projeto

```
hands-on/
├── requirements.md
├── design.md
├── tasks.md
├── requirements.txt
├── demo_flow.py
├── docs/
└── app/
```

## Execucao manual da API

```bash
cd hands-on
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Depois abra:

- http://127.0.0.1:8000/docs

## Ambiente sugerido

- Python 3.11+
- VS Code
- GitHub Copilot e GitHub Copilot Chat

O devcontainer deste repositório já instala as dependências de hands-on automaticamente.

