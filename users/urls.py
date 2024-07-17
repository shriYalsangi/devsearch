from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('add-skill/', views.createSkill, name='add-skill'),
    path('edit-skill/<str:pk>', views.editSkill, name='edit-skill'),
    path('delete-skill/<str:pk>', views.deleteSkill, name='delete-skill'),

    path('', views.profiles, name='profiles'),
    path('user/<str:pk>/', views.UserProfile, name='user-profile'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.viewMessage, name='message'),
    path('send-message/<str:pk>/', views.createMessage, name='send-message'),
]