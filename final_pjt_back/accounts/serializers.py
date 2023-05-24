from rest_framework import serializers
from .models import User


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