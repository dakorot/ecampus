from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_page(request):
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


    context = {}
    return render(request, 'base/login_form.html', context)


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
    return render(request, 'base/feed.html')


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
