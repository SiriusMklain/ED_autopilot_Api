from django.shortcuts import render
from .models import *


def home(request):
    # articles = Article.objects.filter(status_article="active")
    # context = {"articles": articles}
    full_url = request.build_absolute_uri()
    context = {'full_url': full_url}
    return render(request, 'home/index.html', context=context)
