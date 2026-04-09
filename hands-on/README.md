# Hands-On: Spec-Driven Development com GitHub Copilot

## 🎯 Sobre Este Hands-On

Este é um treinamento prático de **Spec-Driven Development (SDD)** usando GitHub Copilot. O foco não é aprender Python ou FastAPI, mas sim praticar o fluxo completo de desenvolvimento orientado por especificações:

**Fluxo SDD:** Especificações → Design → Tarefas → Implementação

### 📋 O Que Você Vai Fazer
- Ler especificações funcionais (`requirements.md`)
- Analisar o design arquitetural (`design.md`)
- Seguir tarefas passo-a-passo (`tasks.md`) usando GitHub Copilot
- Construir uma API REST completa de gestão de tarefas

### 📋 Estrutura

```
hands-on/
├── requirements.md      # Especificação funcional
├── design.md           # Arquitetura e design
├── tasks.md            # Tarefas passo-a-passo
├── requirements.txt    # Dependências Python
├── docs/              # Documentação adicional
└── app/
    ├── main.py        # Entry point (você vai criar)
    ├── models.py      # Modelos Pydantic (você vai criar)
    └── storage.py     # Camada de dados (você vai criar)
```

## 🚀 Como Começar

### 1. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 2. Leia os Documentos (nesta ordem)
1. **requirements.md** - Entenda o que precisa ser feito
2. **design.md** - Entenda como estruturar
3. **tasks.md** - Siga as tarefas passo-a-passo

### 3. Implemente as Tarefas
- Siga cada tarefa em `tasks.md`
- Use os prompts fornecidos com GitHub Copilot
- Teste após cada tarefa

### 4. Rode a Aplicação
```bash
python -m uvicorn app.main:app --reload
```
A API estará disponível em `http://localhost:8000`

### 5. Teste os Endpoints
```bash
# Healthcheck
curl http://localhost:8000/health

# Listar tarefas
curl http://localhost:8000/tarefas

# Criar tarefa
curl -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Minha primeira tarefa"}'
```

## 📚 Objetivos de Aprendizado

Ao completar este hands-on, você terá:
- ✅ Entendido o fluxo Spec-Driven Development (requisitos → design → tarefas → código)
- ✅ Aprendido a usar GitHub Copilot para acelerar implementação
- ✅ Construído uma API REST funcional com FastAPI
- ✅ Praticado boas práticas de separação de responsabilidades
- ✅ Consolidado conhecimento através de hands-on prático

## ⏱️ Tempo Estimado

- **Total**: ~45 minutos (9 tarefas × ~5 min cada)
- Cada tarefa deve levar entre 4-6 minutos
- Inclui testes e validações

## 💡 Dicas

1. **Leia todo o arquivo tasks.md antes de começar** para ter visão geral
2. **Use os prompts exatos** fornecidos em cada tarefa - foram otimizados para Copilot
3. **Teste após cada tarefa** para garantir funcionamento
4. **Não decore código** - foco é aprender o fluxo SDD
5. **Experimente com variações** dos prompts depois que terminar

## 🆘 Precisa de Ajuda?

Se um endpoint não funcionar:
1. Verifique se importou corretamente os módulos
2. Verifique se o arquivo tem a assinatura de função correta
3. Verifique status HTTP esperado
4. Use `python -m uvicorn app.main:app --reload` com `--log-level debug`

## 📖 Referências

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://httpwg.org/specs/rfc7231.html#status.codes)
- [GitHub Copilot Tips](https://bing.com/search?q=github+copilot+tips)

---

**Boa sorte com seu hands-on! 🎯**
