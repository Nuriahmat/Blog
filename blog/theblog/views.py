from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def home(request):
#     return render(request, 'home.html', {})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['post_date']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args)
        context["category_menu"] = category_menu
        return context


# def CategoryView(request, category_name):
#     category_post = Post.objects.filter(category=category_name)
#     return render(request, "categories.html", {'category_name': category_name, 'category_post': category_post})


class CategoryView(ListView):
    model = Post
    template_name = "categories.html"

    def get_context_data(self, *args, **kwargs):
        category_name = self.kwargs['category_name']
        category_menu = Category.objects.all()
        category_post = Post.objects.filter(
            category=self.kwargs['category_name'])
        context = super(CategoryView, self).get_context_data(*args)
        context["category_name"] = category_name
        context["category_post"] = category_post
        context["category_menu"] = category_menu
        return context


class DetailView(DetailView):
    model = Post
    template_name = "detail.html"

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(DetailView, self).get_context_data(*args)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


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
