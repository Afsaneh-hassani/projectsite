from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name='blog'
urlpatterns = [
    
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    
    path('<int:pid>/<str:cat_name>/', blog_view, name='category'),
    path('test/', test_view, name='test'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('search/', blog_search, name='search'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path("rss/feed/", LatestEntriesFeed()),

    
]