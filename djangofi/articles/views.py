from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

@login_required(login_url="accounts:login")
def article_create(request):
    return render(request, 'articles/article_create.html')

def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article': article})
