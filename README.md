# Django Dino Blog

Simple blog created with Django, following Net Ninja's Django tutorial.

## To run (on Windows):

1. Create an environment [env]:
        
        > python -m venv [path]

2. Activate the environment and install django:

        > Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
        > ./[env]/Scripts/activate.ps1
        
3. On the django-proj folder, install the requirements (inlcudes django):

        > pip install -r requirements.txt

4. Finally, on the djangofi root folder, run the server with:

        > python manage.py runserver