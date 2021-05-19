from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/', views.PostsListView.as_view(), name='posts'),
]
