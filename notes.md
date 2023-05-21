
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
    3. Define the element: ```article1.title = '[value]'```
    4. Save the element: ```article1.save()```

- To display all the elements: ```Article.objects.all()``` 

    - Inside the class, we can also add the function **\_\_str\_\_** to define how we want the elements to be displayed

- To get a specific element: ```Article.objects.get([param]=[value])```

## Django Admin Area

- Admin area is by default at **/admin/**

- To create a user with access to admin area, run ```python manage.py createsuperuser``` (mine is sofi, pass sofichan23)

- To manage a new model from within the admin area, we need to register the model in the **admin.py** file inside the corresponding app

## Display dynamic data

1. In the **views** file, send the list of articles to the template as an argument of render

2. In the HTML template, we can use template tags to loop through the articles: ```{% %}``` for code and ```{{ }}``` for outputting data

## Static Files (CSS, JavaScript, Images)

In Django, we need to explicitly set static images up inside our project. We will tell Django to serve up our images, for now.

1. In the main **urls** file, we need to add **staticfiles_urlpatterns** to the known **urlpatterns**

2. Then, in the settings file, we need to set up a **STATICFILES_DIRS** tuple with the path to the directory where we will store the static files

3. We then create the static files directory inside the root directory, as well as the static files

4. Finally, we can add the files to the HTML template using template tags - we import the info using ```{% load static from staticfiles %}```; then, we load the file using a **link**, with href ```{% static '[filename]' %}```

## Advanced Templates

Since we want every page's style to be coherent, there is a lot of info that will be repeated in each template. So, we can make a **base_layout** template and make the others extend from that one.

1. Create the **base_layout** file with the generic code.

2. Where the template specific code should go, we write ```{% block content %} ... {% endblock %}```

3. Then, in the other templates, we add the same template tags ```{% block content %} ... {% endblock %}``` around their content, and we add ```{% extends 'base_layout.html' %}``` at the top.

## Advanced URLs

- To capure a parameter in a URL, we can write ```<var_type:var_name>``` as the received slug in the **urls** file. This will result in passing **var_name** as a parameter to the respective request processing function in the **views** file.

- We can also name specific urls using the **name** parameter in the **path** function. This is useful so we can refer to them when in other files. Additionally, it is useful to namespace our urls by declaring the **app_name** in thet **urls** file.
    - Then we can, for example, add an anchor to the articles' titles and link it to each article's detailed page using ```<a href="{% url 'articles:details' slug=article.slug %}">```.

## Uploading Media

1. Like for static files, we need to declare a **MEDIA_URL** and a **MEDIA_ROOT** in the **settings** file, so that Django knows where to store and find the images.

2. Likewise, we need to add the media files' url patterns to the **urlpatterns** property in the main **urls** file.

3. We need to add an image field to our model and migrate it.

4. Then, we need to output the image in the article details template.

4. Finally, we can add an article with an image to the database using the admin area.