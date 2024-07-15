from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('user/<str:pk>/', views.UserProfile, name='user-profile'),
]