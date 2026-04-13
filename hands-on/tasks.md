# Tarefas: Hands-On SDD com Copilot

Use este arquivo como roteiro de apresentacao ou workshop. O fluxo inteiro foi comprimido para caber em 25 a 30 minutos.

## Como usar este roteiro

- Se a ideia for demonstrar, execute os prompts e mostre a solucao pronta.
- Se a ideia for praticar, use os prompts para pedir ao Copilot que gere ou refine os arquivos.
- Ao final, valide tudo com python demo_flow.py.

Distribuicao sugerida de tempo:

- Etapas 1 e 2: 8 minutos
- Etapas 3 a 5: 12 a 15 minutos
- Etapa 6 e fechamento: 5 a 7 minutos

Nota sobre Spec Kit:

- Nao e necessario para este hands-on.
- O fluxo de especificacao ja esta representado diretamente pelos arquivos requirements.md, design.md e tasks.md.
- Se quiser mostrar maturidade de processo numa versao futura, Spec Kit pode entrar como camada adicional, nao como pre-requisito.

---

## Etapa 1: Ler a especificacao

Objetivo: sair do problema para uma lista objetiva de funcionalidades.

Prompt para o Copilot:

```text
Leia requirements.md e resuma em uma checklist curta: endpoints, validacoes obrigatorias e respostas esperadas.
```

Resultado esperado:

- entendimento claro do CRUD de tarefas
- alinhamento sobre healthcheck
- confirmacao de que a solucao sera em memoria

---

## Etapa 2: Confirmar o design

Objetivo: transformar requisitos em uma estrutura minima.

Prompt para o Copilot:

```text
Com base em requirements.md, proponha a arquitetura minima para a API em FastAPI usando apenas app/main.py, app/models.py e app/storage.py. Explique a responsabilidade de cada arquivo em poucas linhas.
```

Resultado esperado:

- definicao clara de responsabilidades
- entendimento de por que nao existe banco nem service layer neste MVP

---

## Etapa 3: Criar a base da aplicacao

Objetivo: subir a API e comprovar que o projeto inicia.

Prompt para o Copilot:

```text
Crie a base da aplicacao em app/main.py com FastAPI e um endpoint GET /health que retorne {"status": "ok"}. Crie tambem o arquivo requirements.txt com fastapi e uvicorn.
```

Verificacao:

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

---

## Etapa 4: Criar modelos e storage

Objetivo: preparar a estrutura de dados antes dos endpoints.

Prompt para o Copilot:

```text
Crie os modelos Pydantic TarefaCreate, TarefaUpdate e Tarefa em app/models.py. Depois crie app/storage.py com armazenamento em memoria, id sequencial e funcoes criar, listar, obter, atualizar e deletar tarefa.
```

Resultado esperado:

- validacao de titulo e status
- timestamps na tarefa
- ordenacao por tarefa mais recente

---

## Etapa 5: Implementar os endpoints CRUD

Objetivo: conectar requisitos ao comportamento da API.

Prompt para o Copilot:

```text
Implemente em app/main.py os endpoints POST /tarefas, GET /tarefas, GET /tarefas/{id}, PUT /tarefas/{id} e DELETE /tarefas/{id}. Use os modelos Pydantic, chame as funcoes de storage e retorne 404 com {"detail": "Tarefa não encontrada"} quando a tarefa nao existir.
```

Resultado esperado:

- CRUD completo funcional
- codigos HTTP coerentes
- resposta JSON simples para exclusao

---

## Etapa 6: Validar o fluxo completo

Objetivo: demonstrar valor de ponta a ponta.

Prompt para o Copilot:

```text
Crie um script simples de demonstracao que suba a API, execute healthcheck, crie tarefas, liste, detalhe, atualize e delete uma tarefa, imprimindo as respostas no terminal.
```

Verificacao:

```bash
python demo_flow.py
```

Ao final da demo, mostre tambem:

```bash
python -m uvicorn app.main:app --reload
```

Depois abra:

- http://127.0.0.1:8000/docs

---

## Fechamento sugerido

Pergunta para encerrar com o cliente:

```text
Se quisermos evoluir esta base, qual sera a proxima especificacao: filtros, persistencia ou autenticacao?
```


