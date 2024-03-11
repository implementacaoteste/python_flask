from flask import current_app
from modules.gestao_de_tarefa.models.tarefa import Tarefa


def salvar_tarefa_no_bd(tarefa):
    # Obtém a conexão com o banco de dados a partir do objeto Flask global
    mysql = current_app.mysql

    # Executa a operação no banco de dados
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO tabela_tarefas (titulo, descricao) VALUES (%s, %s)", (tarefa.titulo, tarefa.descricao))
    mysql.connection.commit()
    cursor.close()
