from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.views import generic

import views
from .forms import BikeOrderForm
from .models import Bike, Order, Basket


class BikeListView(generic.ListView):

	template_name = 'shop/bikes.html'  # Specify your own template name/location
	context_object_name = 'bikes'  # your own name for the list as a template variable

	def get_queryset(self):
		return Bike.objects.all()


class BikeDetailView(generic.DetailView, generic.edit.FormMixin):

	template_name = 'shop/bike_detail.html'  # Specify your own template name/location
	context_object_name = 'bike'  # your own name for the object as a template variable
	form_class = BikeOrderForm

	def get_queryset(self, *args, **kwargs):
		bike_id = self.kwargs.get('pk')
		return Bike.objects.filter(id=bike_id)

	def get_bike_quantity(self, *args, **kwargs):
		bike_id = self.kwargs.get('pk')
		return Bike.objects.get(id=bike_id).quantity

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = self.get_form()
		return context

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed
		# It should return an HttpResponse
		return views.process_order(self.request)

	def form_invalid(self, form):
		# This method is called when invalid form data has been POSTed
		# It should return an HttpResponse
		return render(self.request, 'shop/bike_detail.html', {'form': form})

	def get_success_url(self):
		return f'/order/{Order.objects.last().id}/'

	def get_initial(self):
		initial = super().get_initial()
		initial['bike_id'] = self.kwargs.get('pk')
		return initial

	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)


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
