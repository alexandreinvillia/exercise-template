# Testes da API de Tarefas

Este arquivo contém scripts para testar a API após implementação.

## Script Bash de Teste Completo

```bash
#!/bin/bash

BASE_URL="http://localhost:8000"

echo "=== Testando API de Tarefas ==="

# 1. Healthcheck
echo "1. Healthcheck:"
curl -s $BASE_URL/health | python3 -m json.tool
echo

# 2. Criar tarefas
echo "2. Criando tarefas:"
curl -s -X POST $BASE_URL/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Estudar Python"}' | python3 -m json.tool
echo

curl -s -X POST $BASE_URL/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Praticar FastAPI","descricao":"Hands-on de SDD"}' | python3 -m json.tool
echo

# 3. Listar tarefas
echo "3. Listando todas as tarefas:"
curl -s $BASE_URL/tarefas | python3 -m json.tool
echo

# 4. Obter tarefa específica
echo "4. Obtendo tarefa ID 1:"
curl -s $BASE_URL/tarefas/1 | python3 -m json.tool
echo

# 5. Atualizar tarefa
echo "5. Atualizando tarefa ID 1:"
curl -s -X PUT $BASE_URL/tarefas/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"concluida"}' | python3 -m json.tool
echo

# 6. Deletar tarefa
echo "6. Deletando tarefa ID 1:"
curl -s -X DELETE $BASE_URL/tarefas/1 | python3 -m json.tool
echo

# 7. Verificar deleção
echo "7. Verificando se tarefa foi deletada:"
curl -s $BASE_URL/tarefas/1
echo

echo "=== Teste concluído ==="
```

## Como executar

1. Salve o script acima como `test_api.sh`
2. Dê permissão: `chmod +x test_api.sh`
3. Execute: `./test_api.sh`

Ou execute os comandos individualmente no terminal.