from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_post/', views.create_post, name='create_post'),
    path('posts/', views.post_list, name='post_list'),
]