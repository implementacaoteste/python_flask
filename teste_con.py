import mysql.connector

MYSQL_HOST = 'db'  # Nome do serviço do banco de dados no Docker Compose
MYSQL_USER = 'erisvaldo'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'db_flask'
SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

def conectar_mysql(host, usuario, senha, banco):
    try:
        # Conectando ao banco de dados
        conexao = mysql.connector.connect(
            host=host,
            user=usuario,
            password=senha,
            database=banco
        )

        if conexao.is_connected():
            print("Conexão bem-sucedida ao MySQL.")
            return conexao

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")

    return None

def criar_tabela_usuario(conexao):
    try:
        cursor = conexao.cursor()

        # Definindo a query SQL para criar a tabela
        criar_tabela_query = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            idade INT
        )
        """

        # Executando a query para criar a tabela
        cursor.execute(criar_tabela_query)
        print("Tabela 'usuario' criada com sucesso.")

    except mysql.connector.Error as erro:
        print(f"Erro ao criar tabela: {erro}")

    finally:
        if cursor:
            cursor.close()

def inserir_usuario(conexao, nome, idade):
    try:
        cursor = conexao.cursor()

        # Definindo a query SQL para inserir um usuário
        inserir_usuario_query = """
        INSERT INTO usuario (nome, idade) VALUES (%s, %s)
        """
        dados_usuario = (nome, idade)

        # Executando a query para inserir o usuário
        cursor.execute(inserir_usuario_query, dados_usuario)
        conexao.commit()
        print("Usuário inserido com sucesso.")

    except mysql.connector.Error as erro:
        conexao.rollback()
        print(f"Erro ao inserir usuário: {erro}")

    finally:
        if cursor:
            cursor.close()

# Exemplo de uso das funções
conexao = conectar_mysql('localhost', MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
if conexao:
    criar_tabela_usuario(conexao)
    inserir_usuario(conexao, "Fabio de SOusa Leal", 30)  # Inserindo um usuário de exemplo
    conexao.close()  # Não se esqueça de fechar a conexão quando terminar
