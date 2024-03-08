FROM python:3.8-slim

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia os arquivos requirements.txt para o diretório de trabalho
COPY requirements.txt ./

# Instala as dependências do Python listadas no requirements.txt
RUN apt-get update && apt-get install -y python3-venv python3-pip && \
    python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copia o diretório do projeto para o diretório de trabalho
COPY projeto/ ./projeto/

# Exponha a porta 5000
EXPOSE 5000

# Define o comando padrão para iniciar o aplicativo Flask
CMD ["bash", "-c", "source /venv/bin/activate && python3 projeto/app/routes.py"]
