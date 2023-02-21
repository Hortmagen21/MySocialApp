from rest_framework import serializers
from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['content', 'author']


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Like
        fields = ['author', 'post']


class LikeByDaySerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()
    likes = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ('date', 'likes')



