from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('books', views.books, name="books"),
    # path('customer', views.customer),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('create', views.create, name="create"),
    path('update/<str:pk>', views.update, name="update"),
]
