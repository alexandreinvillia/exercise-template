# Testes da API de Tarefas

## Forma mais simples

Dentro de hands-on, execute:

```bash
python demo_flow.py
```

Esse script faz a validacao completa do fluxo e nao depende de bash.

## Teste manual com PowerShell

Inicie a API:

```powershell
python -m uvicorn app.main:app --reload
```

Em outro terminal PowerShell, execute:

```powershell
$baseUrl = "http://127.0.0.1:8000"

Invoke-RestMethod -Method Get -Uri "$baseUrl/health"

Invoke-RestMethod -Method Post -Uri "$baseUrl/tarefas" -ContentType "application/json" -Body '{"titulo":"Preparar demo"}'

Invoke-RestMethod -Method Post -Uri "$baseUrl/tarefas" -ContentType "application/json" -Body '{"titulo":"Mostrar SDD","descricao":"Fluxo com Copilot"}'

Invoke-RestMethod -Method Get -Uri "$baseUrl/tarefas"

Invoke-RestMethod -Method Get -Uri "$baseUrl/tarefas/1"

Invoke-RestMethod -Method Put -Uri "$baseUrl/tarefas/1" -ContentType "application/json" -Body '{"status":"concluida"}'

Invoke-RestMethod -Method Delete -Uri "$baseUrl/tarefas/2"
```

## O que verificar

- /health retorna status ok
- POST cria tarefas com id e timestamps
- GET /tarefas retorna a lista ordenada
- GET /tarefas/1 retorna uma tarefa especifica
- PUT altera status para concluida
- DELETE retorna mensagem de sucesso