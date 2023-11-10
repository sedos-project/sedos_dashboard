# SEDOS Dashboard

Dashboard to view and compare scenario data

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Installation (locally)

Follow instructions from https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#setting-up-development-environment
but instead of creating repo via cookiecutter (TOP 3) you have to clone it. Afterwards, you don't have to `git init` the repo (TOP 4), as you cloned it already.

More detailed step by steps instructions based on first user experiences are described below:
1. Install Python, Postgresql and Pycharm Professional with academic license (https://www.jetbrains.com/community/education/#students) on your machine
2. Clone sedos_dashboard repository: <sedos directory path>
3. Clone django_comparison_dashboard repository: <dashboard directory path>
4. Clone django_energysystem_viewer repository: <energysystem directory path>
5. Enter sedos_dasboard directory
6. Change to developer branch: checkout dev
7. Copy SEDOS_Modellstruktur.xlsx into new directory: <sedos directory path>/sedos_dashboard/sedos_dashboard/media
8. Create a virtualenv: python3.11 -m venv <virtual env path>
9. Activate the virtualenv you have just created: source <virtual env path>/bin/activate (or in windows <virtual env path>\Scripts\activate)
10. Install required packages in terminal:
     pip install -r requirements/local.txt
     Additional required packages:
         pip install django-template-partials
         pip install django-htmx
     Add django_comparison_dashboard and django_energysystem_viewer apps in edit-mode to project:
         pip install -e <dashboard directory path>
         pip install -e <energysystem directory path>
11. Activate pre-commit:
     pre-commit install
12. Setup local database:
     createdb --username=postgres gui_db
13. Create environment file .env in sedos_dashboard with the following lines:
      DATABASE_URL=postgres://postgres:postgres@127.0.0.1:5432/gui_db
      CELERY_BROKER_URL=redis://localhost:6379/0
      USE_DOCKER=False
14. Apply migrations:
    export (set on windows) DJANGO_READ_DOT_ENV_FILE=TRUE
    python manage.py migrate
15. Set django run configuration runserver in pycharm:
    set name: runserver
    reference environment variable: DJANGO_READ_DOT_ENV_FILE=TRUE
    set working directory: <sedos directory path>
