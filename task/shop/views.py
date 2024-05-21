from django.views import generic
from .models import Bike


class BikeListView(generic.ListView):

	template_name = 'shop/bikes.html'  # Specify your own template name/location
	context_object_name = 'bikes'  # your own name for the list as a template variable
	#model = Bike  # The model that you want to display in the template

	# This method is used to get the list of objects to be displayed
	# in the template. Here we are getting all the bikes from the database
	# and returning them as a queryset.
	def get_queryset(self):
		return Bike.objects.all()
