from django.db import models

# Create your models here.


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    tagline = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)   
    release_date = models.CharField(max_length=50,null=True)
    # json 시리얼라이즈 오류로 charfield로 변경.
    runtime = models.IntegerField()
    # genres = models.ManyToManyField(Genre)
