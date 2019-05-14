from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Images.as_view(), name="images"),
    path("<int:image_id>/", view=views.ImageDetail.as_view(), name="feed"),
    path("<int:image_id>/likes/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/comment/", view=views.CommentOnImage.as_view(), name="comment_id"),
    path("comments/<int:comment_id>/", view=views.Comment.as_view(), name="comment"),
    path("<int:image_id>/unlikes/", view=views.UnLikeImage.as_view(), name="unlike_image_id"),
    path("search/", view=views.Search.as_view(), name="search"),
    path("<int:image_id>/comments/<int:comment_id>", view=views.ModerateComments.as_view(), name="ModerateComments"),
]


