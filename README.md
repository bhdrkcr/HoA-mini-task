# drf custom login

A mini project about registration, login and admin panel with drf

## Setup

Make sure you have python == 3.9.2 installed and set as environment variable with postgresql13 create a database and user with all privileges on database

- clone project to your computer
- create a venv and activate it

```bash
cd drf-custom-login
python3 -m venv env
source en/bin/activate
```

- create .env file from .env.example
- install dependencies

```bash
pip install -r requirements/development.pip
```

- migrate database

```bash
python manage.py migrate
```

- start server

```bash
python manage.py runserver
```

- go to http://127.0.0.1:8000/
- Rock'n'roll
