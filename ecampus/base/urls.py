from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('', views.home_page, name='home'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/<str:pk>', views.profile_page, name='profile'),
    path('feed/', views.feed_page, name='feed'),
    path('messages/', views.messages_page, name='messages'),
    path('create-message/', views.create_message, name='create-message'),
    path('post/<str:pk>', views.user_post, name='user_post'),
    path('create-post/', views.create_post, name='create-post'),
    path('update-post/<str:pk>', views.update_post, name='update-post'),
    path('delete-post/<str:pk>', views.delete_post, name='delete-post'),
    path('update-comment/<str:pk>', views.update_comment, name='update-comment'),
    path('delete-comment/<str:pk>', views.delete_comment, name='delete-comment'),
    path('performance/', views.performance_page, name='performance'),
    path('grades/', views.grades_page, name='grades'),
    path('create-grade/', views.create_grade, name='create-grade'),
    path('update-grade/<str:pk>', views.update_grade, name='update-grade'),
    path('delete-grade/<str:pk>', views.delete_grade, name='delete-grade'),
    path('examinations/', views.examinations_page, name='examinations'),
    path('documents/', views.documents_page, name='documents'),
    path('subjects-choice/', views.subjects_choice_page, name='subjects-choice'),
    path('subjects-choice/<str:question_pk>/', views.vote, name='vote'),
    path('subjects-choice/<str:question_pk>/results/', views.vote_results, name='vote-results'),
    path('help/', views.help_page, name='help'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)