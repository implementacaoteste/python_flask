import sys
import os
# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(sys.path)

from flask import Flask, render_template, request, redirect, url_for
from modules.gestao_de_tarefa.models.tarefa import Tarefa
from flaskext.mysql import MySQL
from config import Config

# Cria uma instância do Flask
app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)

# Define uma rota para o endpoint "/"
@app.route("/")
def index():
    return render_template("index.html")

# Define uma rota para o endpoint "/cadastro_tarefa"
@app.route("/cadastro_tarefa")
def cadastro_tarefa():
    return render_template("cadastro_tarefa.html")

# Rota para lidar com a submissão do formulário de cadastro de tarefa
@app.route("/submit_tarefa", methods=["POST"])
def submit_tarefa():
    if request.method == "POST":
        # Obter os dados do formulário
        tarefa = Tarefa(request.form["titulo"], request.form["descricao"])

        #aqui você pode coloar a lógica para salvar no banco de dados

        # Redirecionar de volta para a página inicial após o cadastro da tarefa
        return redirect(url_for("index"))
    
# Define uma rota para o endpoint "/cadastro_usuario"
@app.route("/cadastro_usuario")
def cadastro_usuario():
    return render_template("cadastro_usuario.html")

# Executa o aplicativo se este arquivo for o ponto de entrada
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
