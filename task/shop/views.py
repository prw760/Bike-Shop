from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .forms import BikeOrderForm
from .models import Bike, Order, Basket


class BikeListView(generic.ListView):

	template_name = 'shop/bikes.html'  # Specify your own template name/location
	context_object_name = 'bikes'  # your own name for the list as a template variable

	def get_queryset(self):
		return Bike.objects.all()


class BikeDetailView(generic.DetailView):

	template_name = 'shop/bike_detail.html'  # Specify your own template name/location
	form = BikeOrderForm
	context_object_name = 'bike'  # your own name for the object as a template variable

	def get_queryset(self, *args, **kwargs):
		bike_id = self.kwargs.get('pk')
		return Bike.objects.filter(id=bike_id)

	def get_bike_quantity(self, *args, **kwargs):
		bike_id = self.kwargs.get('pk')
		return Bike.objects.get(id=bike_id).quantity


def process_order(request):

	name = request.POST['name']
	surname = request.POST['surname']
	phone_number = request.POST['phone_number']
	bike_id = request.POST['bike_id']

	bike = Bike.objects.get(id=bike_id)

	bike.frame.quantity -= 1
	bike.seat.quantity -= 1
	bike.tire.quantity -= 2
	if bike.has_basket:
		basket = Basket.objects.first()
		basket.quantity -= 1
		basket.save()
	bike.save()

	order = Order(bike=bike, name=name, surname=surname, phone_number=phone_number, status='P')
	order.save()

	return HttpResponseRedirect(f'/order/{order.id}/')


class OrderView(generic.DetailView):

	template_name = 'shop/order.html'  # Specify your own template name/location
	context_object_name = 'order'  # your own name for the object as a template variable

	def get_queryset(self, *args, **kwargs):
		order_id = self.kwargs.get('pk')
		return Order.objects.filter(id=order_id)
