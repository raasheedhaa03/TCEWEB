from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login,name="login"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout"),
    path('main/<int:id>',views.events,name="main"),
    path('club',views.club,name="club"),
    path('clubev/<int:id>',views.clubev,name="clubev"),
    path('social/signup/', views.signup_redirect, name='signup_redirect'),
    path('ach/<int:id>',views.ach,name="ach"),
]
