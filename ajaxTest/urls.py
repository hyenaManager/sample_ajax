from django.urls import path,include
from .views import get,register
urlpatterns = [
    path('home',get,name="home"),
    path('register',register,name="register")
]