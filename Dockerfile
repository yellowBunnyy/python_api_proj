#!/bin/sh

# Pobranie obrazu pythonowego
FROM python:3.8
RUN mkdir -p /usr/src/my_app
WORKDIR /usr/src/my_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=src
ENV FLASK_DEBUG=1
ENV SECRET=SECRET
ENV SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite
EXPOSE 2731:2731

# Zanstalowanie apt zależności netcat gcc
RUN apt-get update \   
    && apt-get clean

# Zainstalowanie zależności pythonowych
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt 

# Skopiowanie apki
COPY . .
RUN python ./create_db.py
RUN flask run --host=0.0.0.0 --port=2731
