from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200,default='user does not provied bio')
    location = models.CharField(max_length=200,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    interests = models.CharField(max_length=200,blank=True)
    twitter_handle = models.CharField(max_length=50, blank=True,default='no twitter')
    facebook_handle = models.CharField(max_length=50, blank=True,default='no facebook')
    instagram_handle = models.CharField(max_length=50, blank=True,default='no instagram')

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


