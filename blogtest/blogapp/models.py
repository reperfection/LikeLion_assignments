from pickle import FALSE
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published', )
    body = models.TextField(blank=FALSE)
    writer = models.CharField(max_length = 10, default='재완')
    
    #기분 선택
    HAPPY = '행복'
    GREAT = '아주좋음'
    GOOD = '좋음'
    SOSO = '그냥저냥'
    DEPRESSED = '우울'
    SAD = '슬픔'
    BAD = '나쁨'
    TERRIBLE = '최악'
    COMFORTABLE = '편안한'
    TODAY_FEELING = [
        (HAPPY, '행복'),
        (GREAT, '아주좋음'),
        (GOOD, '좋음'),
        (SOSO, '그냥저냥'),
        (DEPRESSED, '우울'),
        (SAD, '슬픔'),
        (BAD, '나쁨'),
        (TERRIBLE, '최악'),
        (COMFORTABLE, '편안한'),
    ]
    today_feeling = models.CharField(
        max_length = 50, choices = TODAY_FEELING, null=True)
    
    def __str__(self):
        return self.title