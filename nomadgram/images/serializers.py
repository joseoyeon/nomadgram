from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models
from rest_framework import status
from taggit_serializer.serializers import (TagListSerializerField,TaggitSerializer)

class SmallImageSerializer(serializers.ModelSerializer) : 
    """Used for the notifications"""
    class Meta :
        model = models.Image
        fields = (
            'file',
        )

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta : 
        model = user_models.User
        fields = (
            'username',
            'profile_image',
        )

class CommentSerializer(serializers.ModelSerializer):
    creator = FeedUserSerializer(read_only=True)

    class Meta :
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
            'image',
        )

class LikeSerializer(serializers.ModelSerializer):

    class Meta : 
        model = models.Like
        fields = (
            'creator',
        )

class InputImageSerializer(serializers.ModelSerializer) :

    class Meta : 
        model = models.Image
        fields = [
            'file',
            'location',
            'caption',
        ]

class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    comments = CommentSerializer(many =True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()
    
    class Meta:
        model = models.Image        
        fields = (
        'id',
        'file',
        'location',
        'caption',
        'comments',
        'like_count',
        'creator',
        'tags',
        'created_at',
        )

class CountImageSerializer(TaggitSerializer, serializers.ModelSerializer):

    class Meta:
        model = models.Image  
        fields = (
        'id',
        'file',
        'comment_count',
        'like_count',
        )
