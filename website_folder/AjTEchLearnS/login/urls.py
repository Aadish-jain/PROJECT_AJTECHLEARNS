from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login', views.login,name='login'),
    path('loginuser',views.handlelogin,name="handlelogin")
    # path('logout',views.handleLogout,name="handleLogout"),
    ]