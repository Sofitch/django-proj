from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('date')
    print(request.user)
    return render(request, 'articles/article_list.html', {'articles': articles})

@login_required(login_url="accounts:login")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False) # dont save right away
            article.author = request.user
            article.save() # save article to db
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article': article})
