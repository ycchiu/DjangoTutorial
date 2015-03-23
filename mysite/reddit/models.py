from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    title_text = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    author = models.ForeignKey('auth.User')
    upvote = models.IntegerField(default = 0)
    downvote = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.title_text + ":" + self.url + " by " + author.username ;
