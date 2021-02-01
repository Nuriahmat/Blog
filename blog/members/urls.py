
from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', UserRegistrationView.as_view(), name="register"),
]
