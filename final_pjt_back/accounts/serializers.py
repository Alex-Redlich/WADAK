from rest_framework import serializers
from .models import User

from movies.models import Movie
from communities.models import Comment, Review


class UserSerializer(serializers.ModelSerializer):
    class FollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id','username',)

    followings = FollowingSerializer(many=True, read_only=True)
    followers = FollowingSerializer(many=True,read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only = True)
    followers_count = serializers.IntegerField(source='followers.count', read_only = True)
    
    class Meta:
        model = User
        fields = ('id','username','chingho','current_point','total_point','rank','nickname','intro','today_movie','followings','followings_count','followers','followers_count')
        read_only_fields = ('followings','followings_count','followers','followers_count')


class UserInteractionSerializer(serializers.ModelSerializer):
    class FollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id',)
            
    followings = FollowingSerializer(many=True, read_only=True)
    followers = FollowingSerializer(many=True,read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only = True)
    followers_count = serializers.IntegerField(source='followers.count', read_only = True)
    
    class ReviewIdSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('id',)
            
    class MovieIdSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id',)
    
    class CommentIdSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id',)
    
    like_movies = MovieIdSerializer(many=True,read_only=True)
    like_reviews = ReviewIdSerializer(many=True,read_only=True)
    like_comments = CommentIdSerializer(many=True,read_only=True)
    
    class Meta:
            model = User
            fields = ('today_movie','like_movies','like_reviews','like_comments','followings','followers','followings_count','followers_count')