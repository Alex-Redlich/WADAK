from rest_framework import serializers
from .models import Chingho, User


class UserSerializer(serializers.ModelSerializer):
    class FollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'
            
    followings=FollowingSerializer(many=True, read_only=True)  
    # chinghos=ChinghoSerializer(many=True, read_only=True)   
           
    class Meta:
        model = User

        fields = '__all__'
        
class ChinghoSerializer(serializers.ModelSerializer):
    having_users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Chingho
        fields = '__all__'