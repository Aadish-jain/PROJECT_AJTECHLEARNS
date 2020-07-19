from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # API to post a comment
    path('postComment',views.postComment,name="postComment"),

    
    path('', views.blog,name='blog'),

    path('blog_page/',views.blog_page,name='blog_page'),
    
    path('<str:slug>',views.blogPost,name = 'blogPost'),
    

    ]
    