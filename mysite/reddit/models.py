from django.db import models

class Links(models.Model):
    title_text = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title_text + ":" + self.url;
    