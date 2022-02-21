from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('books', views.books),
    # path('customer', views.customer),
    path('customer/<str:pk>', views.customer),
]
