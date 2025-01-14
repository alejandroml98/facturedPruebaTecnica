FROM python:3.8-slim-bullseye

RUN apt update

RUN apt install nano -y

#Instalación PIPENV como manejador de paquetes
RUN pip install pipenv

#Carpeta base
WORKDIR /apps/queryApp

# instalar dependencias de proyecto
COPY ./queryApp/requirements.txt /apps/queryApp/requirements.txt

RUN pip install -r requirements.txt