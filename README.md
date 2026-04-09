# Hands-On: Spec-Driven Development com GitHub Copilot

Aprenda Spec-Driven Development (SDD) criando uma API REST de gestão de tarefas usando GitHub Copilot no Visual Studio Code.

## Bem-vindo

- **Para quem é**: Desenvolvedores com conhecimento básico de programação que querem aprender desenvolvimento orientado por especificações
- **O que você aprenderá**: Fluxo completo de SDD (especificação → design → tarefas → implementação) usando GitHub Copilot
- **O que você construirá**: API REST completa para gestão de tarefas pessoais com FastAPI
- **Pré-requisitos**:
  - Conhecimento básico de Python
  - Familiaridade com conceitos de API REST
  - Conta GitHub com Copilot habilitado

- **Quanto tempo**: Este exercício leva cerca de 45 minutos para completar.

Neste exercício, você irá:

1. Ler e entender especificações funcionais
2. Analisar o design arquitetural proposto
3. Seguir tarefas passo-a-passo usando GitHub Copilot
4. Implementar uma API REST completa
5. Testar todos os endpoints criados

### Como iniciar este exercício

1. Se quiser usar este material como um exercício para alunos, primeiro copie este repositório para sua conta com o botão **Use this template** no GitHub.
2. Crie um novo repositório a partir deste template:
   - https://github.com/new?template_owner=alexandreinvillia&template_name=exercise-template
3. Abra o repositório copiado no GitHub Codespaces.
4. Navegue para a pasta `hands-on/`
5. Siga as instruções no `README.md` da pasta hands-on

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?repo=alexandreinvillia/exercise-template&devcontainer_path=.devcontainer/devcontainer.json)

> Este repositório é a base do template. Para um exercício de aluno, use primeiro uma cópia do template e, depois, abra o Codespaces na cópia.

### Estrutura do Projeto

```
hands-on/
├── requirements.md      # Especificações funcionais
├── design.md           # Arquitetura e design
├── tasks.md            # Tarefas passo-a-passo
├── requirements.txt    # Dependências Python
├── docs/              # Documentação adicional
└── app/
    ├── __init__.py
    ├── main.py        # Você criará este arquivo
    ├── models.py      # Você criará este arquivo
    └── storage.py     # Você criará este arquivo
```

### Próximos Passos

Após completar o hands-on básico, você pode evoluir a API adicionando:
- Validações mais rigorosas
- Filtros e paginação
- Persistência com banco de dados
- Autenticação e autorização
- Testes automatizados

---

*Este hands-on foi criado usando GitHub Copilot e segue as melhores práticas de Spec-Driven Development.*

