from csv import writer
from email.quoprimime import body_check
from turtle import title
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    writer = models.CharField(max_length = 20, null = True, blank = True, default ="재완")
    feeling = models.CharField(max_length = 50, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title