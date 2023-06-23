from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255,)
    author = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
# Create your models here.
