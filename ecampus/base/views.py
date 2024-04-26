from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Post
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PostForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    return render(request, 'base/login_form.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def home_page(request):
    # context = {}
    return render(request, 'base/home.html')


def profile_page(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'base/profile.html', context)


def feed_page(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'base/feed.html', context)


def user_post(request, pk):
    user_post = Post.objects.get(id=pk)
    # post_messages = user_post.messages_set.all()

    context = {'user_post': user_post}
    return render(request, 'base/post.html', context)


@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.author = request.user
            form.save()
            return redirect('feed')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url='login')
def update_post(request, pk):
    user_post = Post.objects.get(id=pk)
    form = PostForm(instance=user_post)

    if request.user != user_post.author:
        return HttpResponse('You are not the author.')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=user_post)
        if form.is_valid():
            user_post.save()
            return redirect('feed')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    user_post = Post.objects.get(id=pk)
    if request.method == 'POST':
        user_post.delete()
        return redirect('feed')
    context = {'object': user_post}
    return render(request, 'base/delete.html', context)


def messages_page(request):
    return render(request, 'base/messages.html')


def performance_page(request):
    return render(request, 'base/performance.html')


def examinations_page(request):
    return render(request, 'base/examinations.html')


def documents_page(request):
    return render(request, 'base/documents.html')


def subjects_choice_page(request):
    return render(request, 'base/subjects_choice.html')


def help_page(request):
    return render(request, 'base/help.html')
