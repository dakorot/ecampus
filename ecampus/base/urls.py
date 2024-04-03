from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    # path('profile/<str:pk>', views.profile_page, name='profile'),
    path('feed/', views.feed_page, name='feed'),
    path('messages/', views.messages_page, name='messages'),
    path('performance/', views.performance_page, name='performance'),
    path('examinations/', views.examinations_page, name='examinations'),
    path('documents/', views.documents_page, name='documents'),
    path('subjects-choice/', views.subjects_choice_page, name='subjects-choice'),
    path('help/', views.help_page, name='help'),
]
