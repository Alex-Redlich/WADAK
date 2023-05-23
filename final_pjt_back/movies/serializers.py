from rest_framework import serializers
from .models import Movie

class MovieSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','poster_path')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
