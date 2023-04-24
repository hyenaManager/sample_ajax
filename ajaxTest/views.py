from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.

def home(request):
    posts = Post.objects.all()
    pP = UserProfile.objects.get(user = request.user.id)
    return render(request,'home.html',{'user_name':request.user,'posts':posts,"userP":pP})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=password)
            user_profile = UserProfile.objects.create(User=user)
            user_profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = User.objects.get(username=request.user.username)
        post = Post.objects.create(
            title=title,
            content=content,
            user_id = request.user.id
            )
        post.save()
        return redirect('home')
    return render(request,'create_post.html',{'user_name':request.user.username})

def create_userPp(request):
    if request.method == 'POST':
        profile_pict = request.FILES.get('profile_picture')
        userP = UserProfile.objects.get(user=request.user.id)
        userP.profile_pic = profile_pict
        userP.save()
        return redirect('home')
    userP = UserProfile.objects.get(user=request.user.id)
    return render(request,'userProfile.html',{
        "user_profile":userP
    })