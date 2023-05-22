from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE) # because user is also an instance of a model

    def __str__(self):
        return self.title

    def snippet(self):
        SNIPPET_LEN = 100
        snippet = self.body[:SNIPPET_LEN]
        if len(self.body) > SNIPPET_LEN:
            snippet = snippet[:SNIPPET_LEN-3] + '...'
        return snippet