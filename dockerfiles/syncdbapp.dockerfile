FROM python:3.8-slim-bullseye

RUN apt update

RUN apt install nano -y

#Instalación PIPENV como manejador de paquetes
RUN pip install pipenv

#Carpeta base
WORKDIR /apps/syncDBApp

# instalar dependencias de proyecto
#COPY ./commandApp/requirements.txt /apps/commandApp/requirements.txt

#RUN pip install -r requirements.txt