from django.urls import path,include
from .views import home,register
urlpatterns = [
    path('home',home,name="home"),
    path('register',register,name="register")
]