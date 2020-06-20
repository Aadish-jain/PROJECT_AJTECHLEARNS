from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=350)
    phone = models.CharField(max_length = 15)
    email = models.CharField( max_length=254)
    content = models.TextField()