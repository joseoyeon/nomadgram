from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import statuss

class Feed(APIView):
    def get(self, request, format=None):
        user = request.user
        following_users = user.following.all()
        image_list = []

        for following_user in following_users:
            user_images = following_user.images.all()[:2]
            for image in user_images:
                image_list.append(image)
        
        sorted_list = sorted(image_list, key = lambda x: x.created_at, reverse =True)
        serializer = serializers.ImageSerializer(sorted_list, many=True)
        return Response(serializer.data)


class LikeImage(APIView):
    def get(self, request, image_id, format=None):

        user = request.user
        try : 
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=404)

        try:
            preexisiting_like = models.Like.objects.get(
                creator = user,
                image = found_image
            )
            preexisiting_like.delete()
            return Response(status=202)
        except models.Like.DoesNotExist:
            new_like =models.Like.objects.create(
                creator =user,
                image = found_image
            )
            new_like.save()
            return Response(status=200)

class CommentOnImage(APIView): 
    def post(self, request, image_id, format=None) :
        user = request.user
        try:
            found_image =models.Image.Objects.get(id=image_id)
        except: models.Image
        serializer = serializers.CommentSerializer(data=request.data)
        if serializer.is_vaild() :
            serializer.save(creator=user)
            return Response(data=serializer.data, status=201)
        else:
            return Response(data=serializer.errors, status=400)
