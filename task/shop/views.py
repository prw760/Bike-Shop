import http
from django.http import request
from django.views import generic
from .models import Bike


class BikeListView(generic.ListView):

	template_name = 'shop/bikes.html'  # Specify your own template name/location
	context_object_name = 'bikes'  # your own name for the list as a template variable

	def get_queryset(self):
		return Bike.objects.all()


class BikeDetailView(generic.DetailView):

	template_name = 'shop/bike_detail.html'  # Specify your own template name/location
	context_object_name = 'bike'  # your own name for the object as a template variable

	def get_queryset(self, *args, **kwargs):
		bike_id = self.kwargs.get('pk')
		return Bike.objects.filter(id=bike_id)
