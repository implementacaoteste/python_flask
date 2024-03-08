FROM debian:latest

WORKDIR /app

RUN apt update -y && apt install -y python3 python3-venv python3-pip

RUN python3 -m venv /venv 

ENV PATH="/venv/bin:$PATH"

RUN pip install flask-login flask

EXPOSE 5000

CMD ["bash", "-c", "source /venv/bin/activate && python3 routes.py"]