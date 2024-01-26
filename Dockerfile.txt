# syntax=docker/dockerfile:l

FROM python:3.8-slim-buster

WORKDIR / app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirementes.txt

COPY . .

CMD ["python3", "main.py"]