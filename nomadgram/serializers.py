from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):

    images = ImageSerializer()
    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerialalizer(serializers.ModelSerializer):

    images = ImageSerializer()
    class Meta:
        model = modles.Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image        
        fields = '__all__'
