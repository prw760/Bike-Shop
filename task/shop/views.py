from django.http import request, HttpResponseRedirect
from django.views import generic
#from .forms import BikeOrderForm
from .models import Bike


class BikeListView(generic.ListView):

	template_name = 'shop/bikes.html'  # Specify your own template name/location
	context_object_name = 'bikes'  # your own name for the list as a template variable

	def get_queryset(self):
		return Bike.objects.all()


class BikeDetailView(generic.DetailView):

	template_name = 'shop/bike_detail.html'  # Specify your own template name/location
	context_object_name = 'bike'  # your own name for the object as a template variable
	#form = BikeOrderForm

	def get_queryset(self, *args, **kwargs):
		bike_id = self.kwargs.get('pk')
		return Bike.objects.filter(id=bike_id)

	def get_bike_quantity(self, *args, **kwargs):
		bike_id = self.kwargs.get('pk')
		return Bike.objects.get(id=bike_id).quantity


def process_bike_order(p_request, pk):

	if p_request.method == 'POST':

		form = BikeOrderForm(p_request.POST)

		if form.is_valid():

			bike_id = form.cleaned_data['bike_id']
			name = form.cleaned_data['name']
			surname = form.cleaned_data['surname']
			phone_number = form.cleaned_data['phone_number']

			bike = Bike.objects.get(id=bike_id)
			bike.quantity -= 1
			bike.save()

			bike_order = bike.order_set.create(name=name, surname=surname, phone_number=phone_number, bike_id=bike_id)
			bike_order.save()

			return HttpResponseRedirect('/bikes/order-processed/' + str(bike_order.id) + '/')
