from rest_framework import serializers
from . import models

class ImageSerializer(serializers, Serializer):

    class Meta:
        model = models.Image
        fields = '__all__'

class CommentSerializer(serializers.Serializer):

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerialalizer(serializers.Serializer):

    class Meta:
        models = modles.Like
        fields = '__all__'
