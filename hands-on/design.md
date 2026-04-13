# Design: API de Gestao de Tarefas

## Objetivo do design

Manter a arquitetura pequena o suficiente para ser explicada em poucos minutos, mas clara o bastante para mostrar o valor do Spec-Driven Development.

## Arquitetura escolhida

```
Cliente HTTP
   |
FastAPI em app/main.py
   |
Modelos Pydantic em app/models.py
   |
Armazenamento em memoria em app/storage.py
```

Nao existe service layer neste MVP. A decisao foi intencional: reduzir ruído na demonstracao e manter foco no fluxo SDD.

## Componentes

### app/main.py

- inicializa o FastAPI
- expõe /health
- expõe CRUD completo em /tarefas
- traduz erros de negocio simples para HTTP 404

### app/models.py

- define TarefaCreate
- define TarefaUpdate
- define Tarefa
- restringe status para pendente ou concluida
- aplica validacao de tamanho nos campos principais

### app/storage.py

- usa dicionario em memoria
- gera ids sequenciais
- encapsula operacoes CRUD
- retorna tarefas ordenadas da mais recente para a mais antiga

### demo_flow.py

- executa o fluxo end-to-end da demonstracao
- sobe a API automaticamente se necessario
- faz chamadas HTTP reais
- imprime respostas de cada etapa

## Endpoints

| Metodo | Rota | Uso |
|--------|------|-----|
| GET | /health | validar que a API esta no ar |
| POST | /tarefas | criar tarefa |
| GET | /tarefas | listar tarefas |
| GET | /tarefas/{id} | detalhar tarefa |
| PUT | /tarefas/{id} | atualizar tarefa |
| DELETE | /tarefas/{id} | remover tarefa |

## Fluxo de requisicao

1. O cliente envia JSON para a API.
2. FastAPI valida a entrada com Pydantic.
3. O endpoint chama funcoes do storage.
4. O storage devolve a tarefa criada, alterada, listada ou removida.
5. O endpoint retorna uma resposta HTTP adequada.

## Decisoes principais

- Simplicidade primeiro: sem banco, sem autenticacao e sem camadas extras.
- Rastreabilidade: cada endpoint nasce diretamente dos requisitos.
- Demonstrabilidade: tudo pode ser mostrado em poucos comandos.
- Evolucao facil: se a conversa com o cliente pedir proxima fase, a troca do storage por banco real e direta.

## Possiveis evolucoes

- filtro por status em GET /tarefas
- persistencia em SQLite
- testes automatizados com pytest
- autenticacao
