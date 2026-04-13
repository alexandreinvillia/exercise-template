# Requisitos: API de Gestão de Tarefas

## Visão Geral
Desenvolver uma API REST que permita gerenciar tarefas pessoais. O sistema deve ser simples, performático e escalável para suportar usuários adicionando, visualizando, atualizando e deletando tarefas.

## Requisito de Demonstração

- O fluxo precisa ser fácil de executar ao vivo, sem dependência de banco de dados ou infraestrutura externa.
- A solução deve permitir uma demo completa em poucos minutos.

## RF0: Healthcheck

- **O que**: Endpoint para verificar se a API está disponível
- **Entrada**: nenhuma
- **Saída**: `{"status": "ok"}`

## Requisitos Funcionais

### RF1: Criar Tarefa
- **O que**: Endpoint para criar nova tarefa
- **Entrada**: título (string, obrigatório), descrição (string, opcional)
- **Saída**: tarefa criada com ID único, timestamp de criação, status
- **Status padrão**: `pendente`

### RF2: Listar Tarefas
- **O que**: Endpoint para listar todas as tarefas
- **Entrada**: nenhuma (pode adicionar filtro por status depois)
- **Saída**: array de tarefas com todos os campos
- **Ordenação**: mais recentes primeiro

### RF3: Atualizar Tarefa
- **O que**: Endpoint para atualizar tarefa existente
- **Entrada**: ID da tarefa, título ou descrição ou status
- **Saída**: tarefa atualizada
- **Validação**: tarefa deve existir

### RF4: Deletar Tarefa
- **O que**: Endpoint para deletar tarefa
- **Entrada**: ID da tarefa
- **Saída**: confirmação de exclusão
- **Validação**: tarefa deve existir

### RF5: Obter Detalhes da Tarefa
- **O que**: Endpoint para retornar uma tarefa específica
- **Entrada**: ID da tarefa
- **Saída**: dados completos da tarefa
- **Validação**: tarefa deve existir

## Requisitos Não-Funcionais

### RNF1: Performance
- Todas as operações devem responder em <100ms

### RNF2: Disponibilidade
- Sistema deve estar disponível 24/7 durante o hands-on

### RNF3: Simplicidade
- Dados armazenados em memória (Fase 1)
- Estrutura clara e facilmente extensível

### RNF4: Tratamento de Erros
- Retornar status HTTP apropriado
- Mensagens de erro legíveis

## Modelo de Dados

```
Tarefa {
  id: UUID ou inteiro
  titulo: string (1-100 caracteres)
  descricao: string (0-500 caracteres)
  status: enum ["pendente", "concluida"]
  criada_em: timestamp (ISO 8601)
  atualizada_em: timestamp (ISO 8601)
}
```

## Endpoints (Resumo)

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/health` | Verificar saúde da API |
| POST | `/tarefas` | Criar tarefa |
| GET | `/tarefas` | Listar todas |
| GET | `/tarefas/{id}` | Obter detalhes |
| PUT | `/tarefas/{id}` | Atualizar |
| DELETE | `/tarefas/{id}` | Deletar |

## Constraints
- ✅ Foco em prática, não em teoria
- ✅ MVP sem autenticação (Fase 1)
- ✅ Sem persistência em BD (Fase 1)
- ✅ Código deve ser simples e legível
- ✅ Deve ser fácil de demonstrar em reunião
