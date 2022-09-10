from django.urls import path

from users.views import RegisterUserAPIView

urlpatterns = [
    path('signup/', RegisterUserAPIView.as_view(), name="signup"),
]