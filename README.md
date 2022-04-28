# Flask API - COVID vs INFLUENZA analisis

# Discription

Comparing two viruses based on number of infection, hospitalizatin and deaths in Poland.
The analisis covers the yars 2020 - 2021.

## Table of Contents

- [About](#about)
- [How to run API](#api)
- [Folder Structure](#structure)


## About <a name = "about"></a>

Resource Manager API

## How to run API <a name="api"></a>

First install docker https://docs.docker.com/engine/install/ubuntu/, 
next install docker-compose https://docs.docker.com/compose/install/,

enter in the console:
```
> docker-compose build .
> docker-compose up
```

You can then add your environment variables like this:

```
PORT=5000
```

## Folder Structure <a name="structure"></a>

```
├── create_db.py
├── docker-compose.yml
├── Dockerfile
├── docs
│   └── testing.py
├── README.md
├── requirements.txt
└── src
    ├── auth.py
    ├── config.py
    ├── db.sqlite
    ├── __init__.py
    ├── main.py
    ├── models.py
    └── templates
        ├── base.html
        ├── index.html
        ├── login.html
        ├── profile.html
        └── signup.html
```
