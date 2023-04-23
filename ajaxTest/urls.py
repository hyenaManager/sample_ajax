from django.urls import path,include
from .views import home,register,create_post
urlpatterns = [
    path('home',home,name="home"),
    path('register',register,name="register"),
    path('create_post',create_post,name="create_post")
]