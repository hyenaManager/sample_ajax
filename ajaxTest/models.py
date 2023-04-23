from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True,null=True)
    twitter_handle = models.CharField(max_length=50, blank=True,null=True)
    facebook_handle = models.CharField(max_length=50, blank=True,null=True)
    instagram_handle = models.CharField(max_length=50, blank=True,null=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


