from django.db import models


class Streamer(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

# Create your models here.
