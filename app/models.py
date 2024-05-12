from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')


    def __str__(self):
        return self.title

