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
RUN apt install sqlite3

# Zainstalowanie zależności pythonowych
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt 

# Skopiowanie apki
COPY . .
RUN chmod +x run_app.sh

CMD [ "./run_app.sh" ]
