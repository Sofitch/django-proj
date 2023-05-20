
# Net Ninja Django Tutorial - Notes

### To activate the python environment
On folder 'myproj':

    > Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

    > ./djenv/Scripts/activate.ps1

### To run the blog
On root folder:

    > python manage.py runserver


### To create a new app folder

1. Create the new app

        > python manage.py startapp [app]

2. Inside the app folder, create the urls file, the views file, and the templates folder (where templates should be \[app\]/templates/\[app\])

3. Register the app inside the settings file to make sure Django knows about the app: add \[app\] to the 'INSTALLED APPS' list

4. Include the new app urls file inside the main urls

