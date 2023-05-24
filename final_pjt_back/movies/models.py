from django.db import models
from django.conf import settings
# Create your models here.


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    vote_average = models.FloatField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    tagline = models.CharField(max_length=100, null=True)
    backdrop_path = models.CharField(max_length=200, null=True)
    poster_path = models.CharField(max_length=200, null=True)
    release_date = models.CharField(max_length=50, null=True)
    # json 시리얼라이즈 오류로 charfield로 변경.
    runtime = models.CharField(max_length=30,null=True)
    
    # genres = models.ManyToManyField(Genre, related_name="gerne_movies")
    genres = models.ManyToManyField(Genre, related_name="gerne_movies")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", through="Movie_like_users")

class Movie_like_users(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)