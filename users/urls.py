from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, ProfileAPIView, FavoriteAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='register_api'),
    path('login/', LoginAPIView.as_view(), name='login_api'),
    path('profile/<int:pk>/', ProfileAPIView.as_view(), name='profile_api'),
    path('like/<int:pk>/', FavoriteAPIView.as_view(), name='like_api'),
]
