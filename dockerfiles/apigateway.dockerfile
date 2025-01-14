FROM python:3.8-slim-bullseye

RUN apt update

RUN apt install nano -y

#Instalación PIPENV como manejador de paquetes
RUN pip install pipenv

#Carpeta base
WORKDIR /apps/ApiGateway

# instalar dependencias de proyecto
#COPY ./ApiGateway/requirements.txt /apps/ApiGateway/requirements.txt

#RUN pip install -r requirements.txt