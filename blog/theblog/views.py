from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']


def CategoryView(request, category_name):
    category_post = Post.objects.filter(category=category_name)
    return render(request, "categories.html", {'category_name': category_name, 'category_post': category_post})


class DetailView(DetailView):
    model = Post
    template_name = "detail.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'
    # fields = ('title', 'body')


class updatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"


class deletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = '__all__'
