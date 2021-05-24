from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/', views.PostsListView.as_view(), name='posts'),
    path('tag/<str:slug>/', views.PostsByTag.as_view(), name='tag'),
    path('category/<str:slug>/', views.PostsByCategory.as_view(), name='category'),
    path('about/', views.AboutAsView.as_view(), name='about')
]
