from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('users', views.users),
    path('about', views.about)
]
