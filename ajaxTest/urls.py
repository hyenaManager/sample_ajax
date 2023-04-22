from django.urls import path,include
from .views import get,register
urlpatterns = [
    path('ajax',get,name="get"),
    path('register',register)
]