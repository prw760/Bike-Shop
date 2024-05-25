from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .forms import BikeOrderForm
from .models import Bike, Order


class BikeListView(generic.ListView):

	template_name = 'shop/bikes.html'  # Specify your own template name/location
	context_object_name = 'bikes'  # your own name for the list as a template variable

	def get_queryset(self):
		return Bike.objects.all()


class BikeDetailView(generic.DetailView):

	template_name = 'shop/bike_detail.html'  # Specify your own template name/location
	form_class = BikeOrderForm
	context_object_name = 'bike'  # your own name for the object as a template variable

	def get_queryset(self, *args, **kwargs):
		bike_id = self.kwargs.get('pk')
		return Bike.objects.filter(id=bike_id)

	def get_bike_quantity(self, *args, **kwargs):
		bike_id = self.kwargs.get('pk')
		return Bike.objects.get(id=bike_id).quantity


class ProcessOrderView(generic.FormView):

	template_name = 'shop/order.html'  # Specify your own template name/location
	form_class = BikeOrderForm
	context_object_name = 'order'  # your own name for the object as a template variable

	def get_queryset(self, *args, **kwargs):
		order_id = self.kwargs.get('pk')
		return Order.objects.filter(id=order_id)

	def get_context_data(self, form):

		name = form.cleaned_data['name']
		surname = form.cleaned_data['surname']
		phone_number = form.cleaned_data['phone_number']
		bike_id = form.cleaned_data['bike_id']

		bike = Bike.objects.get(id=bike_id)

		order = Order(bike=bike, name=name, surname=surname, phone_number=phone_number, status='P')
		order.save()

		bike.frame.quantity -= 1
		bike.seat.quantity -= 1
		bike.tire.quantity -= 2
		if bike.has_basket:
			bike.basket.quantity -= 1
		bike.save()

		return HttpResponseRedirect("/order/" + str(order.id) + "/")


class OrderView(generic.DetailView):

	template_name = 'shop/order.html'  # Specify your own template name/location
	context_object_name = 'order'  # your own name for the object as a template variable

	def get_queryset(self, *args, **kwargs):
		order_id = self.kwargs.get('pk')

