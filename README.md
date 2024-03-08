# Meu Projeto

Bem-vindo ao projeto Meu Projeto! Este projeto é uma aplicação Python que demonstra uma estrutura organizada e boas práticas de desenvolvimento.

## Organização do Projeto

O projeto está organizado da seguinte maneira:

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

