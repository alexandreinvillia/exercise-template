# Tarefas: Spec-Driven Hands-On

Siga as tarefas abaixo em ordem. Cada tarefa deve levar ~5 minutos. Use o GitHub Copilot para acelerar a implementação.

---

## ✅ Tarefa 1: Setup Inicial

**Objetivo**: Criar estrutura base do projeto

**Instruções**:
1. Criar o arquivo `app/__init__.py` (arquivo vazio)
   
   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   > ```prompt
   > Crie o arquivo app/__init__.py vazio no diretório app
   > ```

2. Criar o arquivo `app/main.py` com inicialização mínima do FastAPI
   
   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   > ```prompt
   > Crie o arquivo app/main.py que inicialize uma aplicação FastAPI com um healthcheck endpoint GET /health que retorna {"status": "ok"}
   > ```

3. Criar o arquivo `requirements.txt` com dependências
   
   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   > ```prompt
   > Crie o arquivo requirements.txt com as dependências fastapi e uvicorn
   > ```

**Resultado Esperado**:
```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
# Servidor rodando em http://localhost:8000
```

**Verificação**:
```bash
curl http://localhost:8000/health
# {"status":"ok"}
```

---

## ✅ Tarefa 2: Criar Modelos de Dados

**Objetivo**: Definir estrutura de Tarefa com Pydantic

**Instruções**:
1. Criar o arquivo `app/models.py`
2. Definir classes: `TarefaCreate`, `Tarefa`
3. Usar Pydantic para validação

**Resultado Esperado**:
Arquivo `models.py` contendo modelos com type hints completos

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
> ```prompt
> Crie modelos Pydantic para uma API de tarefas. Crie duas classes:
> - TarefaCreate: com campo titulo (string obrigatório) e descricao (string opcional)
> - Tarefa: com id (int), titulo, descricao, status (string: "pendente" ou "concluida"), criada_em e atualizada_em (datetime)
> ```

**Verificação**:
```python
from app.models import TarefaCreate
t = TarefaCreate(titulo="Minha tarefa")  # OK
t = TarefaCreate(descricao="sem titulo")  # Erro esperado
```

---

## ✅ Tarefa 3: Criar Camada de Armazenamento

**Objetivo**: Implementar "banco de dados" em memória

**Instruções**:
1. Criar o arquivo `app/storage.py`
2. Definir dicionário global para armazenar tarefas
3. Criar funções CRUD (criar, ler, atualizar, deletar)

**Resultado Esperado**:
Arquivo com funções: `criar_tarefa()`, `listar_tarefas()`, `obter_tarefa()`, `atualizar_tarefa()`, `deletar_tarefa()`

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
> ```prompt
> Crie o arquivo app/storage.py que simule um banco de dados em memória para tarefas.
> 
> Requisitos:
> - Use um dicionário global `tarefas = {}` para armazenar
> - Crie função `criar_tarefa(titulo, descricao)` que retorna Tarefa com id auto-incrementado
> - Crie função `listar_tarefas()` que retorna lista de tarefas ordenadas por data (mais recentes primeiro)
> - Crie função `obter_tarefa(id)` que retorna tarefa ou None
> - Crie função `atualizar_tarefa(id, **kwargs)` que atualiza campos
> - Crie função `deletar_tarefa(id)` que remove e retorna True/False
> 
> Use datetime.now() para timestamps
> ```

**Verificação**:
```python
from app.storage import criar_tarefa, listar_tarefas
t = criar_tarefa("Tarefa 1", "Descrição")
assert t.id == 1
assert len(listar_tarefas()) == 1
```

---

## ✅ Tarefa 4: Criar Endpoint POST /tarefas

**Objetivo**: Implementar criação de tarefa via API

**Instruções**:
1. Abrir `app/main.py`
2. Importar modelos e storage
3. Criar rota POST que recebe `TarefaCreate` e retorna `Tarefa`

**Resultado Esperado**:
Endpoint funcional que cria tarefa

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
> ```prompt
> Em app/main.py, crie um endpoint POST /tarefas que:
> - Recebe um JSON com titulo e descrição (use TarefaCreate)
> - Chama storage.criar_tarefa()
> - Retorna a tarefa criada com status 201
> - Use @app.post("/tarefas", response_model=Tarefa, status_code=201)
> ```

**Verificação**:
```bash
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Estudar SDD"}'
  
# Retorna: {"id":1,"titulo":"Estudar SDD","descricao":null,"status":"pendente","criada_em":"...","atualizada_em":"..."}
```

---

## ✅ Tarefa 5: Criar Endpoint GET /tarefas

**Objetivo**: Listar todas as tarefas

**Instruções**:
1. Adicionar rota GET em `main.py`
2. Retornar lista de tarefas

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
> ```prompt
> Em app/main.py, crie um endpoint GET /tarefas que:
> - Chama storage.listar_tarefas()
> - Retorna uma lista de Tarefa (response_model=List[Tarefa])
> - Status 200
> ```

**Verificação**:
```bash
curl http://localhost:8000/tarefas
# [{"id":1,"titulo":"Estudar SDD","descricao":null,"status":"pendente",...}]
```

---

## ✅ Tarefa 6: Criar Endpoint GET /tarefas/{id}

**Objetivo**: Obter detalhes de uma tarefa específica

**Instruções**:
1. Adicionar rota GET com parâmetro de path
2. Tratar caso "não encontrado"

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
> ```prompt
> Em app/main.py, crie um endpoint GET /tarefas/{id} que:
> - Recebe o id como parâmetro de path (path parameter)
> - Chama storage.obter_tarefa(id)
> - Se encontrar, retorna a Tarefa com status 200
> - Se não encontrar, retorna {"detail":"Tarefa não encontrada"} com status 404
> - Use from fastapi import HTTPException
> ```

**Verificação**:
```bash
curl http://localhost:8000/tarefas/1
# {"id":1,...}

curl http://localhost:8000/tarefas/999
# {"detail":"Tarefa não encontrada"}
```

---

## ✅ Tarefa 7: Criar Endpoint PUT /tarefas/{id}

**Objetivo**: Atualizar uma tarefa existente

**Instruções**:
1. Adicionar rota PUT
2. Receber campos opcionais para atualizar
3. Validar se tarefa existe

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
> ```prompt
> Em app/models.py, crie um modelo TarefaUpdate com:
> - titulo: Optional[str] = None
> - descricao: Optional[str] = None
> - status: Optional[str] = None
> 
> Em app/main.py, crie um endpoint PUT /tarefas/{id} que:
> - Recebe TarefaUpdate
> - Valida se tarefa existe (404 se não)
> - Atualiza apenas os campos fornecidos
> - Retorna a tarefa atualizada com status 200
> ```

**Verificação**:
```bash
curl -X PUT http://localhost:8000/tarefas/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"concluida"}'
  
# Retorna tarefa com status atualizado
```

---

## ✅ Tarefa 8: Criar Endpoint DELETE /tarefas/{id}

**Objetivo**: Deletar uma tarefa

**Instruções**:
1. Adicionar rota DELETE
2. Retornar mensagem de confirmação

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
> ```prompt
> Em app/main.py, crie um endpoint DELETE /tarefas/{id} que:
> - Valida se tarefa existe (404 se não)
> - Chama storage.deletar_tarefa(id)
> - Retorna {"mensagem":"Tarefa deletada com sucesso"} com status 200
> ```

**Verificação**:
```bash
curl -X DELETE http://localhost:8000/tarefas/1
# {"mensagem":"Tarefa deletada com sucesso"}

curl http://localhost:8000/tarefas/1
# {"detail":"Tarefa não encontrada"}
```

---

## ✅ Tarefa 9: Testar Fluxo Completo

**Objetivo**: Validar que toda API funciona end-to-end

**Instruções**:
1. Criar o arquivo `test_api.sh` ou `test_api.py`
2. Executar sequência de requests:
   - POST para criar 3 tarefas
   - GET para listar todas
   - GET para obter uma específica
   - PUT para atualizar
   - DELETE para remover

**Resultado Esperado**:
Todos os requests retornam status esperado

**Script de Teste (bash)**:
```bash
# Criar tarefas
curl -X POST http://localhost:8000/tarefas -H "Content-Type: application/json" -d '{"titulo":"Tarefa 1"}'
curl -X POST http://localhost:8000/tarefas -H "Content-Type: application/json" -d '{"titulo":"Tarefa 2","descricao":"Com descrição"}'
curl -X POST http://localhost:8000/tarefas -H "Content-Type: application/json" -d '{"titulo":"Tarefa 3"}'

# Listar
curl http://localhost:8000/tarefas | python -m json.tool

# Detalhe
curl http://localhost:8000/tarefas/1 | python -m json.tool

# Atualizar
curl -X PUT http://localhost:8000/tarefas/1 -H "Content-Type: application/json" -d '{"status":"concluida"}'

# Deletar
curl -X DELETE http://localhost:8000/tarefas/1

# Verificar deleção
curl http://localhost:8000/tarefas/1
```

---

## 🎓 Próximas Evoluções (Fase 2+)

Após completar, você pode adicionar:
- ✅ Validações mais rigorosas (comprimento de strings, etc)
- ✅ Filtro de status em GET /tarefas?status=concluida
- ✅ Ordenação customizável
- ✅ Persistência com SQLite
- ✅ Autenticação com JWT


