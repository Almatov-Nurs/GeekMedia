from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .service import PostsFilter
from .models import Posts, MultiMedia
from .paginations import PostsResultsSetPagination, MediaResultsSetPagination
from .serializer import PostSerializer, PostsSerializer, MultiMediaSerializer


class PostsListAPIView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    pagination_class = PostsResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostsFilter


class PostsDetailAPIView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"


class MultiMediaAPIView(ListAPIView):
    queryset = MultiMedia.objects.all()
    serializer_class = MultiMediaSerializer
    pagination_class = MediaResultsSetPagination
    filter_backends = ()
