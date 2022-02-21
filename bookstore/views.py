from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {
        'customers': customers,
        'orders': orders
    }
    return render(request, 'bookstore/dashboard.html', context)

def books(request):
    books = Book.objects.all()
    return render(request, 'bookstore/books.html', { 'books': books })

def customer(request):
    return render(request, 'bookstore/customer.html')
