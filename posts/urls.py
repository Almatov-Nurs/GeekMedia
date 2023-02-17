from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import PostsListAPIView, PostsDetailAPIView

urlpatterns = [
    path('posts/', PostsListAPIView.as_view(), name="post_list_api"),
    path('posts/<int:id>/', PostsDetailAPIView.as_view(), name="post_detail_api"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
