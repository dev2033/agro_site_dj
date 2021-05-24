from django import template

from blog.models import Post, Tag, Category


register = template.Library()


@register.inclusion_tag('include/last_posts.html')
def get_last_posts(cnt=3):
    """Выводит наиболее просматриваемые посты (по умолчанию - 3)"""
    posts = Post.objects.order_by('-id')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('include/last_post_for_footer.html')
def get_last_posts_for_footer(cnt=2):
    """
    Выводит наиболее просматриваемые посты
    для подвала сайта(по умолчанию - 2)
    """
    posts = Post.objects.order_by('-id')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('include/tags.html')
def get_tags():
    """Выводит облако тегов"""
    tags = Tag.objects.all()
    return {'tags': tags}


@register.inclusion_tag('include/categories.html')
def get_categories():
    """Выводит категории"""
    categories = Category.objects.all()
    return {'categories': categories}