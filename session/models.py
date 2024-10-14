from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')


    def number_of_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_images/', default='default.png', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


    def like_count(self):
        return self.liked_by.count()