from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from .models import Post, Category, Tag


class HomeView(View):
    """Главная страница"""
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/home_page.html')


class PostsListView(ListView):
    """Список постов"""
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """Конкретный пост"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
