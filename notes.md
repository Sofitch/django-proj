
# Net Ninja Django Tutorial - Notes

## General
- To activate the python environment, run ```Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; > ./djenv/Scripts/activate.ps1```.

- To run the blog, run ```python manage.py runserver```


## Django apps

1. Create a new app with ```python manage.py startapp [app]```

2. Inside the app folder, create the urls file, the views file, and the templates folder (where templates should be \[app\]/templates/\[app\])

3. Register the app inside the settings file to make sure Django knows about the app: add \[app\] to the 'INSTALLED APPS' list

4. Include the new app urls file inside the main urls

## Django models

A model corresponds to a single table in a database. Each type of data (Articles, Users, etc) is represented by it's own model. In python, models are a Class.

## Migrations

Django has some built-in models that it automatically creates (admin, auth, etc). We start by migrating those with ```python manage.py migrate```. Then, we can migrate our Article Model:

1. Create a migration to the created models with ```python manage.py makemigrations```.

2. Mirror our models to a database table with ```python manage.py migrate```.

3. Every time we make or change a model, we will have to repeat steps 2 and 3.

