from django.shortcuts import redirect, render

from bookstore.forms import OrderForm
from .models import *
from django.forms import ModelForm, inlineformset_factory

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    pending_orders = orders.filter(status="Pending").count()
    delivered_orders = orders.filter(status="Delivered").count()
    inprogress_orders = orders.filter(status="In progress").count()
    out_orders = orders.filter(status="Pending").count()
    context = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
        'inprogress_orders': inprogress_orders,
        'out_orders': out_orders,
    }
    return render(request, 'bookstore/dashboard.html', context)

def books(request):
    books = Book.objects.all()
    return render(request, 'bookstore/books.html', { 'books': books })

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    number_orders = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'number_orders': number_orders
    }
    return render(request, 'bookstore/customer.html', context)

# def create(request):
#     form = OrderForm()
#     if request.method == 'POST':
#         print(request.POST)
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/home')
#     context = { 'form': form }
#     return render(request, 'bookstore/order_form.html', context)

def create(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('book', 'status'))
    customer = Customer.objects.get(id = pk)
    formset = OrderFormSet(instance=customer)
    if request.method == 'POST':
        if formset.is_valid():
            formset.save()
            return redirect('/home')
    context = { 'formset': formset }
    return render(request, 'bookstore/order_form.html', context)

def update(request, pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = { 'form': form }
    return render(request, 'bookstore/order_form.html', context)

def delete(request, pk):
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        form = OrderForm(request.post, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = { 'order': order }
    return render(request, 'bookstore/delete_form.html', context)
