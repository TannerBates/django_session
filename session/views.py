from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post, Like, Profile, User, Comment
from .forms import PostForm, CommentForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.annotate(comments_count=Count('comments')).all()
    return render(request, 'post_list.html', {'posts': posts})



@login_required(login_url='/login/')
def like_post(request, id):
    post = get_object_or_404(Post, pk=id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER')) # redirect back to previous page



@login_required(login_url='/login/')
def like_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.user in comment.liked_by.all():
        comment.liked_by.remove(request.user)
    else:
        comment.liked_by.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('post_list')



@login_required(login_url='/login/')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})





@login_required(login_url='/login/')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(request, 'profile.html', {'user': user, 'posts': posts})



@login_required(login_url='/login/')
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments_count = post.comments.count()
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', id=post.id)

    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments_count': comments_count,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'post_detail.html', context)