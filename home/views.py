from django.shortcuts import render
from .models import *


def home(request):
    # articles = Article.objects.filter(status_article="active")
    # context = {"articles": articles}
    return render(request, 'home/index.html')
