# Meu Projeto

Bem-vindo ao projeto Meu Projeto! Este projeto é uma aplicação Python que demonstra uma estrutura organizada e boas práticas de desenvolvimento.

## Organização do Projeto

O projeto está organizado da seguinte maneira:

```plaintext
meu_projeto/
├── app/
│ ├── init.py
│ ├── routes.py
│ └── templates/
│ ├── index.html
│ ├── cadastro_tarefa.html
│ └── cadastro_usuario.html
├── modules/
│ ├── init.py
│ ├── autenticacao/
│ │ ├── init.py
│ │ ├── autenticacao_routes.py
│ │ ├── autenticacao_bll.py
│ │ └── autenticacao_dal.py
│ ├── gestao_de_tarefa/
│ │ ├── init.py
│ │ ├── tarefa_routes.py
│ │ ├── bll/
│ │ │ └── tarefa_bll.py
│ │ ├── dal/
│ │ │ └── tarefa_dal.py
│ │ └── models/
│ │ └── tarefa.py
│ └── gestao_de_usuario/
│ ├── init.py
│ ├── usuario_routes.py
│ ├── bll/
│ │ └── usuario_bll.py
│ ├── dal/
│ │ └── usuario_dal.py
│ └── models/
│ └── usuario.py
├── tests/
│ ├── init.py
│ ├── test_autenticacao.py
│ ├── test_gestao_de_tarefa.py
│ └── test_gestao_de_usuario.py
├── docs/
│ ├── guia_do_usuario.md
│ └── api_reference.md
├── dockerfile
├── .gitignore
└── readme.md
```

- **app/**: Contém os arquivos relacionados à aplicação principal.
  - **\_\_init\_\_.py**: Arquivo de inicialização da aplicação.
  - **routes.py**: Arquivo contendo as rotas da aplicação.
  - **templates/**: Diretório contendo os templates HTML.

- **modules/**: Contém os diferentes módulos funcionais do projeto.
  - **autenticacao/**: Módulo responsável pela autenticação de usuários.
  - **gestao_de_tarefa/**: Módulo responsável pela gestão de tarefas.
  - **gestao_de_usuario/**: Módulo responsável pela gestão de usuários.
  - Dentro de cada módulo, há subdiretórios para a lógica de negócios (`bll`), acesso a dados (`dal`) e modelos de dados (`models`).

- **tests/**: Contém os casos de teste para os diferentes módulos do projeto.

- **docs/**: Contém a documentação do projeto.
  - **guia_do_usuario.md**: Guia do usuário.
  - **api_reference.md**: Referência de API.

- **dockerfile**: Arquivo para configuração do ambiente Docker.
- **.gitignore**: Arquivo contendo padrões de arquivos a serem ignorados pelo Git.
- **readme.md**: Este arquivo, contendo informações sobre o projeto.

## Padrões de Nomenclatura

- **Módulos e Diretórios**: Utilizam o padrão snake_case, com nomes descritivos e separados por underline. Exemplo: `gestao_de_tarefa`.
- **Arquivos Python**: Utilizam o padrão snake_case para os nomes dos arquivos e PascalCase para os nomes das classes. Exemplo: `tarefa_bll.py`, `TarefaBLL`.
- **Variáveis e Atributos**: Utilizam o padrão snake_case para os nomes das variáveis e atributos.
- **Funções e Métodos**: Utilizam o padrão snake_case para os nomes das funções e métodos.
- **Constantes**: Utilizam letras maiúsculas separadas por underline. Exemplo: `TAMANHO_MAXIMO`.

## Gitflow

Este projeto segue o modelo de fluxo de trabalho Gitflow para gerenciar o desenvolvimento de novos recursos, correções de bugs e releases. O Gitflow é um fluxo de trabalho de branching que fornece uma estrutura robusta para colaboração em projetos de grande escala.

### Principais Branches

- **main**: Representa a versão de produção do software. Os commits nesta branch refletem o estado atual do código em produção.
- **develop**: Branch de desenvolvimento principal. Novos recursos e correções de bugs são integrados nesta branch antes de serem mesclados na main.
- **feature/**: Branches de recursos individuais. Cada nova funcionalidade é desenvolvida em uma branch separada a partir de `develop`. Quando concluída, a branch de recurso é mesclada de volta para `develop`.
- **release/**: Branches de preparação para uma nova versão. Criadas a partir de `develop`, elas são usadas para finalizar os detalhes da próxima release. Quando pronta, a branch de release é mesclada para `main` e `develop`.
- **hotfix/**: Branches de correção de bugs críticos em produção. Estes são criados a partir de `main`, corrigem o problema e são mesclados de volta para `main` e `develop`.

### Fluxo de Trabalho Básico

1. **Iniciar um novo recurso**: Criar uma branch de recurso a partir de `develop`.
2. **Desenvolver o recurso**: Fazer commits na branch de recurso enquanto desenvolve a nova funcionalidade.
3. **Concluir o recurso**: Solicitar revisão de código, fazer ajustes conforme necessário e mesclar a branch de recurso de volta para `develop`.
4. **Preparar para release**: Criar uma branch de release a partir de `develop` para preparar uma nova versão.
5. **Corrigir bugs**: Se bugs forem descobertos na branch de release, corrigi-los em branches de hotfix a partir de `main`.
6. **Concluir a release**: Mesclar a branch de release de volta para `main` e `develop`.
7. **Implantar em produção**: A partir da main, criar tags para versões específicas e implantar em produção.

### Recursos Adicionais

- **Git Flow Cheat Sheet**: Um guia útil para comandos Gitflow: [Git Flow Cheat Sheet](https://danielkummer.github.io/git-flow-cheatsheet/)

Ao seguir o Gitflow, esperamos manter um fluxo de trabalho consistente e organizado durante todo o ciclo de vida do projeto.
