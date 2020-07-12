from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 1000)
    pubished = models.DateTimeField()
    image = models.ImageField(upload_to = 'media/')
    body = models.TextField()

    def __str__(self):
        return self.title