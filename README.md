# SEDOS Dashboard

Dashboard to view and compare scenario data

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Installation (locally)

Follow instructions from https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#setting-up-development-environment
but instead of creating repo via cookiecutter (TOP 3) you have to clone it. Afterwards, you don't have to `git init` the repo (TOP 4), as you cloned it already.

More detailed step by steps instructions based on first user experiences are described below:
0. Install Python, Postgresql and Pycharm Professional with academic license (https://www.jetbrains.com/community/education/#students) on your machine
1. Clone both repositories into one directory at: <directory path>
2. Change to developer branch: checkout dev
3. Copy SEDOS_Modellstruktur.xlsx into new directory: <directory path>/sedos_dashboard/sedos_dashboard/media
4. Create a virtualenv: python3.11 -m venv <virtual env path>
5. Activate the virtualenv you have just created: source <virtual env path>/bin/activate (or in windows <virtual env path>\Scripts\activate)
6. Install required packages in terminal:
	cd <directory path>/sedos_dashboard
	pip install -r requirements/local.txt
	Additional required packages:
		pip install django-template-partials
		pip install django-htmx
	pre-commit install
7. Setup local database:
	createdb --username=postgres gui_db
8. Apply migrations:
	export (set on windows) DATABASE_URL=postgres://postgres:postgres(password)@127.0.0.1:5432/gui_db
	export (set on windows) CELERY_BROKER_URL=redis://localhost:6379/0
	export (set on windows) USE_DOCKER=False
	python manage.py migrate
9. Create environment file .env in sedos_dashboard with the following lines:
	DATABASE_URL=postgres://postgres:postgres@127.0.0.1:5432/gui_db
	CELERY_BROKER_URL=redis://localhost:6379/0
	USE_DOCKER=False
10. Set django run configuration runserver in pycharm:
	set name: runserver
	reference environment variable: DJANGO_READ_DOT_ENV_FILE=TRUE
	set working directory: <directory path>/sedos_dashboard
