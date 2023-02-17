from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Posts
from .service import PostsFilter
from .paginations import PostsResultsSetPagination
from .serializer import PostSerializer, PostsSerializer


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
