from rest_framework import serializers
from .models import Review, Comment

from accounts.models import User
from accounts.serializers import UserSerializer

from movies.models import Movie
from movies.serializers import MovieSimpleSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only =True)
    like_users = UserSerializer(many = True, read_only =True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only = True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review','user',)
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('review',None)
        return rep


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSimpleSerializer(read_only=True)
    
    comments = CommentSerializer(many=True, read_only = True)
    comments_count = serializers.IntegerField(source='comments.count', read_only = True)
    
    user = UserSerializer(read_only =True)
    like_users = UserSerializer(many = True, read_only =True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only = True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','users','like_users',)


