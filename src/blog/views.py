from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from .models import Post, Category, Tag, About


class HomeView(ListView):
    """Главная страница"""
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home_page.html'
    paginate_by = 6


class PostsListView(ListView):
    """Список постов"""
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 8


class PostDetailView(DetailView):
    """Конкретный пост"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'


class PostsByTag(ListView):
    """Выводит записи по тегу"""
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: ' + str(
            Tag.objects.get(slug=self.kwargs['slug']))
        return context


class PostsByCategory(ListView):
    """Выводит записи по категории"""
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по категории: ' + str(
            Category.objects.get(slug=self.kwargs['slug']))
        return context


class AboutAsView(View):
    """Вывод информации на странице 'О нас'"""
    def get(self, request, *args, **kwargs):
        info = About.objects.all()
        context = {'info': info}
        return render(request, 'blog/about.html', context)














