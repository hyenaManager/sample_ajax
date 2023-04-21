from django.urls import path,include
import views
urlpatterns = [
    path('ajax',views.get),
]