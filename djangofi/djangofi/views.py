from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html') # set the templates dir in settings.py

def about(request):
    return render(request, 'about.html')
