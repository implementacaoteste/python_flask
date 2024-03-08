# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# db = SQLAlchemy()

# class Tarefa(db.Model):
#     __tablename__ = 'tarefa'

#     id = db.Column(db.Integer, primary_key=True)
#     titulo = db.Column(db.String(100), nullable=False)
#     descricao = db.Column(db.Text, nullable=False)
#     data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
#     def __init__(self, titulo, descricao):
#         self.titulo = titulo
#         self.descricao = descricao

#     def __repr__(self):
#         return f'<Tarefa {self.id}: {self.titulo}>'

class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def __repr__(self):
        return f"Tarefa(titulo={self.titulo}, descricao={self.descricao})"