# Design: API de Gestão de Tarefas

## Arquitetura de Alto Nível

```
┌─────────────────┐
│   Cliente HTTP  │
└────────┬────────┘
         │
    ┌────▼──────┐
    │  FastAPI  │ (Framework)
    └────┬──────┘
         │
    ┌────▼────────────────┐
    │   Routes/Endpoints  │ (Controllers)
    └────┬────────────────┘
         │
    ┌────▼────────────────┐
    │   Service Layer     │ (Business Logic)
    └────┬────────────────┘
         │
    ┌────▼────────────────┐
    │   In-Memory Store   │ (Data)
    └─────────────────────┘
```

## Componentes

### 1. **main.py** (Entry Point)
- Inicializa a aplicação FastAPI
- Define configurações globais

### 2. **models.py** (Data Models)
```python
from pydantic import BaseModel
from datetime import datetime

class TarefaCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    status: str  # "pendente" ou "concluida"
    criada_em: datetime
    atualizada_em: datetime
```

### 3. **storage.py** (Data Layer)
Simulação de banco de dados em memória:
- Dicionário que armazena tarefas: `{id: Tarefa}`
- Gerador de IDs sequenciais
- Funções CRUD básicas

### 4. **routes.py** (API Endpoints)
- POST `/tarefas` → criar
- GET `/tarefas` → listar
- GET `/tarefas/{id}` → detalhe
- PUT `/tarefas/{id}` → atualizar
- DELETE `/tarefas/{id}` → deletar

### 5. **responses.py** (Handlers)
Tratamento de erros e respostas padrão:
- 200: Sucesso
- 201: Recurso criado
- 404: Não encontrado
- 400: Requisição inválida
- 500: Erro interno

## Fluxo de Requisição

```
1. Cliente faz requisição HTTP
   ↓
2. FastAPI roteia para endpoint correto
   ↓
3. Validação automática com Pydantic
   ↓
4. Função route chama serviço
   ↓
5. Serviço manipula dados no storage
   ↓
6. Resposta retorna ao cliente
```

## Stack Tecnológico

| Camada | Tecnologia | Propósito |
|--------|-----------|----------|
| Framework | FastAPI | API REST moderna |
| Validação | Pydantic | Schemas e validação |
| Servidor | Uvicorn | ASGI server |
| Linguagem | Python 3.10+ | Desenvolvimento rápido |

## Decisões de Design

✅ **Simplicidade Primeiro**: Sem ORM, sem autenticação, sem banco real  
✅ **Modularização**: Separação clara de responsabilidades  
✅ **Type Hints**: Código legível e self-documented  
✅ **Pydantic**: Validação de entrada automática  
✅ **Status HTTP Corretos**: Comunicação clara com cliente

## Próximas Evolições

- **Fase 2**: Adicionar validações mais rigorosas
- **Fase 3**: Integrar com SQLite
- **Fase 4**: Adicionar autenticação JWT
