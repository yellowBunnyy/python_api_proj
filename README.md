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
> docker-compose up

when shows up:

Starting python_api_proj_flask_api_service_1 ... done
Attaching to python_api_proj_flask_api_service_1
flask_api_service_1  |  * Serving Flask app 'src' (lazy loading)
flask_api_service_1  |  * Environment: production
flask_api_service_1  |    WARNING: This is a development server. Do not use it in a production deployment.
flask_api_service_1  |    Use a production WSGI server instead.
flask_api_service_1  |  * Debug mode: on
flask_api_service_1  |  * Running on all addresses (0.0.0.0)
flask_api_service_1  |    WARNING: This is a development server. Do not use it in a production deployment.
flask_api_service_1  |  * Running on http://127.0.0.1:5000
flask_api_service_1  |  * Running on http://172.21.0.2:5000 (Press CTRL+C to quit)
flask_api_service_1  |  * Restarting with stat
flask_api_service_1  |  * Debugger is active!
flask_api_service_1  |  * Debugger PIN: 260-536-389

do:

http://127.0.0.1:5000 pres Ctrl + left mouse click
```

You can then add your environment variables like this:

```
PORT=5000
```

## Folder Structure <a name="structure"></a>

```
> tree -I "env|__pycache__|*.ora|*.ora~" # exclude files to show tree
.
├── create_db.py
├── data_scraper
│   ├── create_csv.ipynb
│   ├── download_urls.py
│   ├── extract_data.py
│   └── requirements.txt
├── data_sets
│   ├── cov.csv
│   ├── influenza.csv
│   ├── pickledf
│   │   ├── covid.pickle
│   │   ├── influenza.pickle
│   │   ├── __init__.py
│   │   └── show_polts.py
│   └── prepare_data.ipynb
├── docker-compose.yml
├── Dockerfile
├── docs
│   └── show_doc.sh
├── README.md
├── requirements.txt
├── run_app.sh
└── src
    ├── auth.py
    ├── config.py
    ├── database
    │   └── db.sqlite
    ├── __init__.py
    ├── main.py
    ├── models.py
    ├── static
    │   ├── covid.png
    │   └── influenza.png
    └── templates
        ├── base.html
        ├── index.html
        ├── login.html
        ├── profile.html
        └── signup.html
```
