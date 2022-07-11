from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('data published')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.title