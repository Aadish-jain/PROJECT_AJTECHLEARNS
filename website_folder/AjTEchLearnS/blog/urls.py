from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.blog,name='blog'),
    path('blog_page/',views.blog_page,name='blog_page'),
    path('<str:slug>',views.blogPost,name = 'blogPost'),
    ]