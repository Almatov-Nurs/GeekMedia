from django.urls import path

from .views import PostsListAPIView, PostsDetailAPIView, MultiMediaAPIView

urlpatterns = [
    path('posts/', PostsListAPIView.as_view(), name="post_list_api"),
    path('posts/<int:id>/', PostsDetailAPIView.as_view(), name="post_detail_api"),
    path('media/', MultiMediaAPIView.as_view(), name="multi_media_api"),
]
