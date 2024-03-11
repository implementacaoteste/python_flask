class Config:
    DEBUG = True
    SECRET_KEY = 'sua_chave_secreta'
    MYSQL_HOST = 'db'  # Nome do serviço do banco de dados no Docker Compose
    MYSQL_USER = 'erisvaldo'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'db_flask'
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
