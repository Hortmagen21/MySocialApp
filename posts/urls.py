from django.urls import path
from .views import PostCreate, LikePost, DisLikePost, LikeList

urlpatterns = [
    path('post_create/', PostCreate.as_view(), name='post_create'),
    path('like_post/', LikePost.as_view(), name="like_post"),
    path('dislike_post/<int:post>', DisLikePost.as_view(), name="dislike_post"),
    path('likes/', LikeList.as_view(), name="likes"),
]