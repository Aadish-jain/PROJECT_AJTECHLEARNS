from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=350)
    content = models.TextField()
    author = models.CharField(max_length=200)
    slug = models.CharField(max_length = 250)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
