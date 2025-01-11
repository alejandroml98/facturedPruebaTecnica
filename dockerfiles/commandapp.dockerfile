FROM python:3.8-slim-bullseye

RUN apt update

RUN apt install nano -y

#Instalación PIPENV como manejador de paquetes
RUN pip install pipenv

#Carpeta base
WORKDIR /apps/commandApp

# instalar dependencias de proyecto
#COPY ./commandApp/Pipfile ./django-project/Pipfile.lock ./
#RUN pipenv install --system --deploy