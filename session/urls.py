from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_post/', views.create_post, name='create_post'),
    path('like/<int:id>/', views.like_post, name='like_post'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # path('posts/', views.post_list, name='post_list'),
]