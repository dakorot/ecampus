from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('', views.home_page, name='home'),
    # path('profile/<str:pk>', views.profile_page, name='profile'),
    path('feed/', views.feed_page, name='feed'),
    path('messages/', views.messages_page, name='messages'),
    path('post/<str:pk>', views.user_post, name='user_post'),
    path('create-post/', views.create_post, name='create-post'),
    path('update-post/<str:pk>', views.update_post, name='update-post'),
    path('delete-post/<str:pk>', views.delete_post, name='delete-post'),
    path('performance/', views.performance_page, name='performance'),
    path('examinations/', views.examinations_page, name='examinations'),
    path('documents/', views.documents_page, name='documents'),
    path('subjects-choice/', views.subjects_choice_page, name='subjects-choice'),
    path('help/', views.help_page, name='help'),
]
