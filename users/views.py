from .models import User
from posts.models import Posts
from rest_framework import status, views
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializer import RegistrationSerializer, LoginSerializer, ProfileSerializer


class RegistrationAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(**serializer.data)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)

            return Response(data={"id": user.id,
                                  "first_name": user.first_name,
                                  "last_name": user.last_name,
                                  "refresh": str(refresh),
                                  "access": str(access)}, status=status.HTTP_200_OK
                            )


class ProfileAPIView(views.APIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = self.serializer_class(
            user, many=False, context={"request": request}
        ).data
        return Response(data=serializer, status=status.HTTP_200_OK)


class FavoriteAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        if request.user.is_authenticated:
            post = get_object_or_404(Posts, pk=pk)
            request.user.like.add(post)
            request.user.save()
            return Response(data={"message": "Success liked!"}, status=status.HTTP_202_ACCEPTED)
        return Response(data={"message": "Authorization failed"}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        if request.user.is_authenticated:
            post = get_object_or_404(Posts, pk=pk)
            request.user.like.remove(post)
            request.user.save()
            return Response(data={"message": "Like remove!"}, status=status.HTTP_202_ACCEPTED)
        return Response(data={"message": "Authorization failed"}, status=status.HTTP_401_UNAUTHORIZED)
