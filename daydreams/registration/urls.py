from django.urls import path, include
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('login/', views.login, name='login'),
    path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
    path('welcome/', views.welcome, name='welcome'),
    path('', views.signup, name='signup'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('info/', views.info, name='info')
]
