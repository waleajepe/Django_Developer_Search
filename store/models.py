from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blanck=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	image = models.ImageField(null=True, blank=True)
	digital = models.BooleanField(default=False, null=True, blank=True)

	# @property
	# def imageUrl(self):
	# 	try:
	# 		url = self.image.url
	# 	except:
	# 		url = ''
	# 	return url

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.self.get_total for item in orderitems])
		return total

	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
	address = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	zip_code = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address



