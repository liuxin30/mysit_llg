from django.urls import path

from . import views

app_name = 'llg'
urlpatterns = [
    path('<int:category_pk>', views.index, name='index'),
    path('detail/<int:article_pk>', views.detail, name='detail'),
]