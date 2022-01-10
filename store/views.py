from django.shortcuts import render
from . models import *

# Create your views here.

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {
		'get_cart_total': 0,
		'get_cart_items': 77,
		}

	context = {
	'items':items,
	'order':  order
	}
	print('*********')
	print(request.user)
	
	print('*********')
	return render(request, 'store/cart.html', context)

def store(request):
	products = Product.objects.all()
	context = {
	'products': products
	}
	return render(request, 'store/store.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)
