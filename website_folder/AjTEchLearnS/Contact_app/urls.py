from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.contact_app),
    path('contact_form/',views.contact_form,name="contact_form")
    ]