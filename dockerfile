FROM python:3.8-slim

# Define o diretório de trabalho como /app
WORKDIR /app
ENV FLASK_APP=projeto/app/routes.py

# Copia os arquivos requirements.txt e o Dockerfile para o diretório de trabalho
COPY requirements.txt ./

# Instala as dependências do Python listadas no requirements.txt
RUN apt update -y && apt install -y python3 python3-venv python3-pip && \
    python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Exponha a porta 5000
EXPOSE 5000

# Define o comando padrão para iniciar o aplicativo Flask
CMD ["/bin/bash", "-c", "source /venv/bin/activate && python3 app/routes.py"]
