from django.urls import path
from . import views
from .models import Article

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<slug:slug>', views.article_details, name='details')
]
