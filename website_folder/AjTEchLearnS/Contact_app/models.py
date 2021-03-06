from django.db import models

# Create your models here.
class Contact_app(models.Model):
    name = models.CharField(max_length=350)
    phone = models.CharField(max_length = 15)
    email = models.CharField(max_length=250)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - '+ self.email