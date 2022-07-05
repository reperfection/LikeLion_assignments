from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('data published')
    content = models.TextField()
    
    def __str__(self):
        return self.title