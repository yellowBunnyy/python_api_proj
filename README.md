# Flask API - COVID vs INFLUENZA analisis

# Discription

Comparing two viruses based on number of infection and deaths in Poland.
The analisis covers the yars 2020 - 2021.


## Table of Contents

- [About](#about)
- [Used technologies](#technologies)
- [How to run API](#api)
- [Folder Structure](#structure)


## About <a name = "about"></a>

This project have three steaps.
I. In step one we decided to get data from two diffrent sources:
COVID:
https://covid19.who.int/WHO-COVID-19-global-data.csv
Influenza:
http://wwwold.pzh.gov.pl/oldpage/epimeld/grypa/index.htm

In frist case we download a .csv file so it was easy, but in second case for extract data we were forced to use external library `tabula` for obtain data which we needed because data was on .pdf.
So we decide create data scraper which is included in this project look at [Folder Structure](#structure)

II. In second step downloaded data had to be adapted to the needs of our project and we make preprocessing our data.
This preprocessing include:
- fill n/a data
- change data types
- obtain the necessary data from downloaded data

At the end of the preprocessing we pilcke DataFrames for low usage memory.

III. Create API + database

This step was responsible for creating API using `Flask` and connect with data base using `sqlite`.
Data base holds users, password, names and emails necessary for login and look at data comparing.

IV. Create visulaization

After wehere user login our service is redirected to the page where we can see the ploted data.
We decide to use `plotly` for create plots shows compare data.

Above project is working on `docker` containers where API and Database have separated cointaners.


## Used technologies and libraries <a name="technologies"></a>

Python:
- flask==2.1.1
- pandas==1.4.1
- numpy==1.22.3
- matplotlib==3.5.1
- python-dotenv==0.20.0
- flask-sqlalchemy==2.5.1
- flask-login==0.6.0
- plotly-express==0.4.1

Docker


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
│   │   └── __init__.py
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
    ├── generate_plots.py
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
