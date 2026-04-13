# Hands-On: Spec-Driven Development com GitHub Copilot

Este material foi ajustado para dois cenários:

1. Demo curta com cliente, em 15 a 20 minutos.
2. Workshop guiado com Copilot, em 25 a 30 minutos.

O objetivo continua o mesmo: mostrar o fluxo de SDD de ponta a ponta.

especificacao -> design -> tarefas -> implementacao -> validacao

## O que sera demonstrado

- Como transformar requisitos em uma implementacao pequena e objetiva.
- Como usar o GitHub Copilot para sair de artefatos de especificacao e chegar em codigo executavel.
- Como validar o resultado com um fluxo completo de API REST.

## Sobre Spec Kit

Spec Kit pode ajudar quando voce quer padronizar a criacao e a manutencao dos artefatos de especificacao em times maiores ou em fluxos mais longos.

Para este hands-on, ele nao e obrigatorio.

Motivo:

- o objetivo aqui e demonstrar o fluxo de SDD, nao a ferramenta de governanca da especificacao
- os tres artefatos principais ja estao explicitos em requirements.md, design.md e tasks.md
- adicionar Spec Kit aumentaria a explicacao inicial e consumiria tempo da janela de 25 a 30 minutos

Quando vale incluir Spec Kit em uma proxima versao:

- quando o cliente quiser ver padronizacao de templates
- quando houver varias squads compartilhando o mesmo processo
- quando a conversa evoluir de demo para adoção operacional

## Estrutura

```
hands-on/
├── requirements.md      # O que a API precisa fazer
├── design.md            # Como a solucao foi estruturada
├── tasks.md             # Roteiro guiado para usar com Copilot
├── requirements.txt     # Dependencias Python
├── demo_flow.py         # Script unico para demonstracao end-to-end
├── docs/
│   └── testes.md        # Testes manuais e via PowerShell
└── app/
    ├── __init__.py
    ├── main.py
    ├── models.py
    └── storage.py
```

## Modo 1: Demo Rapida

No terminal, dentro de hands-on:

```bash
pip install -r requirements.txt
python demo_flow.py
```

Esse script:

- sobe a API se ela ainda nao estiver rodando
- executa healthcheck
- cria tarefas
- lista, detalha, atualiza e remove
- encerra o servidor automaticamente quando ele foi iniciado pelo script

## Modo 2: Workshop Guiado com Copilot

1. Leia requirements.md
2. Leia design.md
3. Abra tasks.md
4. Execute as tarefas com o Copilot
5. Valide com python demo_flow.py

Tempo sugerido:

- 3 minutos para contexto e requisitos
- 5 minutos para design
- 12 a 15 minutos para implementacao guiada
- 5 minutos para validacao e fechamento

## Rodando manualmente

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Links uteis durante a demo:

- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs

## Sequencia sugerida para apresentar ao cliente

1. Mostrar requirements.md e explicar o escopo em menos de 2 minutos.
2. Mostrar design.md e destacar a simplicidade da arquitetura.
3. Abrir tasks.md e explicar como o Copilot guia a implementacao.
4. Executar python demo_flow.py.
5. Abrir Swagger para reforcar que a API ficou pronta e navegavel.

## Resultado esperado

Ao final da demonstracao, o cliente deve enxergar:

- um fluxo claro de SDD
- uma API funcionando de verdade
- prompts simples e reaproveitaveis com Copilot
- uma base pequena o suficiente para discutir em reuniao
