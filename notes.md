
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

## User registration

### Signup

1. Create accounts app and add it to **INSTALLED_APPS**.

2. Create **urls** file inside the app and set its patterns (in our case, a signup url). Then, include the urls in the main **urls** file. Create the respective views functions in the **views** file and then the **templates** folder, as well as the templates.

While we could create the signup template from scratch and then handle the authentication in the server ourselves, Django comes with a built-in user creation form (with validation and hints).

3. To use it, we first need to import the form in the **views** file. Then, we can create an instance of the form and then pass it to the template.

4. In the template, we can display the form inside a form tag. We set the action var of the form to post to the signup url. Additionally, we need to send the CSRF token with the form (and whenever we make a POSt request). Then, we only need to add an input field for the user to signup.

5. In the **signup_view** function, we now need to distinguish if the request was a GET or a POST. If it was a POST, we retrieve the user data, validate it and save it to the database.

6. We get the user from the form, and then we login the user, using Django's built-in login function.

7. Finally, we redirect to the main page (in our case, the article list).

[comment]: <> (user created: sauropod, rexopod, raptorpod, stegopod; pass podpod12)

### Login

To make a login page, we follow similar steps to 3-7 (inside the accounts app), since Django also has a built-in login form **AuthenticationForm**. We just add the login URL, the login view function, and the login html template.

### Logout

Logout URLs are usually accessed with a POST request. Django already knows which user is logged in, so it will just log that user out.

1. To make the logout page, we follow the same steps (adding a logout URL and a views function).

2. Then, we add a logout button to the base layout. To do so, we add a **nav** tag inside the header, and inside it we make a **list**, where one element is the logout **form**. This form should redirect to the logout url. Inside the form, we add the necessary **CSRF token**, and the logout **button**.

## User-only page

To restrict a page to logged in users only, we add the Django **login_required** decorator to that page's view.

If the user is redirected to the login page, we will then want to redirect the user back to the restricted page. The Django login decorator puts additional info (a 'next' param) in the login url: we can use it to know if the login page was called by a decorator, and which page the user was trying to access.

    1. We first need to change the login html template to look for a **request.GET.next** and, if it exists, add a hidden input type with the value of the next param, so that it is sent to the view function when the user logs in.

    2. We then handle the information on the login_view function

## Model forms

We want to allow a user to create new articles, which is done using a model form. In Django, a model form is a class that inherits from **django.forms.ModelForm** (just like the AuthenticationForm, for example, which is pre-built). 

1. We thus create a **forms** file inside article, where we will define our model forms.

2. Inside that class, we define a subclass **Meta**, where we define which model and which fields will be present in the form.

3. We then create an instance of the model form in the **views** file and send it to the HTML file.

4. In the HTML file, we display the form as usual (since our form will be receiving a media file, we need to add ```enctype="multipart/form-data"``` to our HTML form). 

5. Finally, back in the **views** file, we handle the form data. If the request is a POST, and the data is valid, we save the new article to the database.

