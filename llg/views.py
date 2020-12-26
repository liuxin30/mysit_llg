from django.shortcuts import render, get_object_or_404
from .models import Category, Article
# Create your views here.
def index(request):
    article_list = Article.objects.all()

