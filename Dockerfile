# syntax=docker/dockerfile:1
# Pobranie obrazu pythonowego
FROM python:3.8
RUN mkdir -p /usr/my_app
WORKDIR /usr/my_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=src
ENV FLASK_DEBUG=1


EXPOSE 5000

# Zanstalowanie apt zależności netcat gcc
RUN apt-get update \
    && apt-get clean

# Zainstalowanie zależności pythonowych
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt 

# Skopiowanie apki
COPY . .
RUN python ./create_db.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000" ]
