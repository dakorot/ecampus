from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('students/', views.get_students),
    path('students/<str:pk>', views.get_student),
    path('choices/', views.get_choices),
]