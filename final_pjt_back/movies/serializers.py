from rest_framework import serializers
from .models import Movie, Genre

from accounts.models import User
from accounts.serializers import UserSerializer

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','poster_path','title')

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many = True, read_only = True)
    like_users = UserSerializer(many=True, read_only=True)
    like_users_count = serializers.IntegerField(source='like_users.count', read_only = True)
    class Meta:
        model = Movie
        fields = '__all__'
        
