
from django.urls import path
# from . import views
from .views import HomeView, DetailView, AddPostView, updatePostView, deletePostView, AddCategoryView, CategoryView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('detail/<int:pk>', DetailView.as_view(), name="detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', updatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', deletePostView.as_view(), name="delete_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:category_name>', CategoryView, name="category"),
]
