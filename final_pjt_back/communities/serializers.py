from rest_framework import serializers
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review','user')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('review',None)
        return rep

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id','title','rating')
        read_only_fields = ('movie','users','like_users')


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only = True)
    comments_count = serializers.IntegerField(source='comments.count', read_only = True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','users','like_users')


