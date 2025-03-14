from django.urls import path
from .views import *

app_name = "wiki"

urlpatterns = [
    path('wiki/articles', articles_list,name= 'articles_list'),
    path('wiki/article/<int:pk>',article_detail,name='articles_detail')
]
