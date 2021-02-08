
from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="profile"),
    path('<int:pk>/edit_profile_page/',
         EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_profile/',
         CreateProfilePageView.as_view(), name="create_profile"),
]
