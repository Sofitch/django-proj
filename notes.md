
# Net Ninja Django Tutorial - Notes

## General
- To activate the python environment, run ```Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; > ./djenv/Scripts/activate.ps1```.

- To run the blog, run ```python manage.py runserver```

> Note: commands to use on Windows Powershell

## Django apps

1. Create a new app with ```python manage.py startapp [appname]```

2. Inside the app folder, create the urls file, the views file, and the templates folder (where templates should be **appname**/templates/**appname**)

3. Register the app inside the settings file to make sure Django knows about the app: add **app** to the INSTALLED_APPS list

4. Include the new app urls file inside the main urls

## Django models

A model corresponds to a single table in a database. Each type of data (Articles, Users, etc) is represented by it's own model. In python, models are a Class.

## Migrations

Django has some built-in models that it automatically creates (admin, auth, etc). We start by migrating those with ```python manage.py migrate```. Then, we can migrate our Article Model:

1. Create a migration to the created models with ```python manage.py makemigrations```.

2. Mirror our models to a database table with ```python manage.py migrate```.

3. Every time we make or change a model, we will have to repeat steps 2 and 3.

## Django ORM

The ORM is built-in into Django to interact with the database using the model.

- To test the ORM, we can open an interactive shell with ```python manage.py shell```.

- To add an element to the database on the interactive shell:
    1. Import the model: ```from articles.models import Article```
    2. Create the element: ```article1 = Article()```
    3. Define the element: ```article1.title = 'Totoro'```
    4. Save the element: ```article1.save()```

- To display all the elements: ```Article.objects.all()``` 

    - Inside the class, we can also add the function **\_\_str\_\_** to define how we want the elements to be displayed

## Django Admin Area

- Admin area is by default at **/admin/**

- To create a user with access to admin area, run ```python manage.py createsuperuser``` (mine is sofi, pass sofichan23)

- To manage a new model from within the admin area, we need to register the model in the **admin.py** file inside the corresponding app