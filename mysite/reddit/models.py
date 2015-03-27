from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Link(models.Model):
    title_text = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    author = models.ForeignKey('auth.User')
    pub_date = models.DateTimeField('date published', default =timezone.now)
    upvote = models.IntegerField(default = 0)
    downvote = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.title_text + ":" + self.url;

class Comment(models.Model):
    content_text = models.TextField()
    link = models.ForeignKey(Link)
    author = models.ForeignKey('auth.User')
    pub_date = models.DateTimeField('date published', default =timezone.now)

    def __str__(self):
        return self.content_text+ " for " + self.link.title_text;
