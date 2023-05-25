from django.db import models
from django.conf import settings
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    
    title = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comments")
    
    content = models.CharField(max_length=50)