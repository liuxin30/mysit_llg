from django.shortcuts import render, get_object_or_404
from .models import Category, Article


# Create your views here.
def index(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    print(category)
    article_list = Article.objects.filter(category=category)
    context = {
        "article_list": article_list
    }
    return render(request, "llg/index.html", context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        "article": article
    }
    return render(request, "llg/detail.html", context)
