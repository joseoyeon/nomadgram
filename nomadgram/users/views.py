from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class ExploreUsers(APIView):
    def get(self,request,formet=None):
        last_five = models.User.objects.all().order_by('-date_joined')[:5]
        serializer = serializers.ListUserSerializer(last_five, many=True)
        return Response(data=serializer.data, status=200)

class FollowUser(APIView):
    def post(self, request, user_id, format=None) :
        user = request.user
        try:
            user_to_follow= models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response (status = 404)

        user.following.add(user_to_follow)
        user.save()
        return Response(status =200)

class UnFollowUser(APIView):
    def post(self, request, user_id, format=None) :
        user = request.user
        try:
            user_to_follow= models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response (status = 404)

        user.following.remove(user_to_follow)
        user.save()
        return Response(status =200)

class UserProfile(APIView) :
    def get(self, request, username, format=None):
        
        try :
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status  =404)
        
        serializer = serializers.UserProfileSerializer(found_user)

        return Response(data=serializer.data, status=200)

class UserFollowers(APIView):
    def get(self, request, username, format=None) : 
        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist : 
            return Response(status= 404)
        
        user_followers = found_user.followers.all()
        serializer = serializers.ListUserSerializer(
            user_followers, many=True)
        return Response(data = serializer.data, status = 200)

class UserFollowing(APIView):
    def get(self, request, username, format=None) : 
        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist : 
            return Response(status= 404)
        
        user_following = found_user.following.all()
        serializer = serializers.ListUserSerializer(
            user_following, many=True)
        return Response(data = serializer.data, status = 200)

class Search(APIView) : 
    def get(self, request, format=None) :
        username = request.query_params.get('username',None)
        
        if username is not None : 
            users = models.User.objects.filter(username__istartswith=username)
            serializer = serializers.ListUserSerializer(users,many=True)
            return Response(data=serializer.data, status=200)
        else : 
            return Response( status =404)

""" def UserFollowingFBC(request, username) : 
    if request.method == 'GET':
        '''request.POST.get('key', value)
        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist : 
            return Response(status= 404)
        
        user_following = found_user.following.all()
        serializer = serializers.ListUserSerializer(
            user_following, many=True)
        return Response(data = serializer.data, status = 200) """
