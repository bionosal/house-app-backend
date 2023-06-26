from django.db import models


class Streamer(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def vote(self, v):
        match v:
            case 'upvote':
                self.upvote += 1
            case 'downvote':
                self.downvote += 1
            case _:
                raise ValueError('Vote invalid')
# Create your models here.
