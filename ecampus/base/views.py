from django.shortcuts import render
from .models import Profile


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
