from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="user-home"),
    path('login', views.loginview, name="user-login"),
    path('logout', views.logoutviews, name = "user-logout")
]