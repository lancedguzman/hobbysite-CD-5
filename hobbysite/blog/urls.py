from django.urls import path
from .views import list_view, detail_view

app_name = 'blog'

urlpatterns = [
   path('blog/articles/', list_view, name='list_view'),
   path('blog/articles/<int:category_id>/', detail_view, name='detail_view')
]
