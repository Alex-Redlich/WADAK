from rest_framework import serializers
from .models import Chingho, User


class UserSerializer(serializers.ModelSerializer):
    class FollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id','username',)

    followings=FollowingSerializer(many=True, read_only=True)
    followers=FollowingSerializer(many=True,read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only = True)
    followers_count = serializers.IntegerField(source='followers.count', read_only = True)

    # chinghos=ChinghoSerializer(many=True, read_only=True)   
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('chingho',)
        
# class ChinghoSerializer(serializers.ModelSerializer):
#     having_users = UserSerializer(many=True, read_only=True)
#     class Meta:
#         model = Chingho
#         fields = '__all__'