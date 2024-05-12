from django.urls import path

from .views import create_post, read_post, read_blog_post, update_post

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('', read_post, name='read_post'),
    path('post/<int:id>/', read_blog_post, name='read_blog'),
    path('post/<int:id>/update/', update_post, name='update_post')


]