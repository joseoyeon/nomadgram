from django.urls import path
from . import views

app_name = "explore"
urlpatterns = [
    path("explore/", view=views.ExploreUsers.as_view(), name="explore_user"),
    path("<int:user_id>/follow/", view=views.FollowUser.as_view(), name="follow_user"),
    path("<int:user_id>/unfollow/", view=views.UnFollowUser.as_view(), name="unfollow_user"),
    path("<username>/followers/", view=views.UserFollowers.as_view(), name="user_followers"),
    path("<username>/following/", view=views.UserFollowing.as_view(), name="user_following"),
    path("search/", view=views.Search.as_view(), name="user_search"),
    path("<username>/", view=views.UserProfile.as_view(), name="user_profile"),
]

'''
app_name = "images"
urlpatterns = [
    path("", view=views.Feed.as_view(), name="feed"),
    path("<int:image_id>/like/", view=views.LikeImage.as_view(), name="image_id"),
    path("<int:image_id>/comment/", view=views.CommentOnImage.as_view(), name="comment_id"),
    path("comments/<int:comment_id>/", view=views.Comment.as_view(), name="comment")
]
'''