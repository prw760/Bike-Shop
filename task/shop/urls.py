from django.urls import path
from django.shortcuts import redirect
from .views import BikeListView, BikeDetailView, process_bike_order


urlpatterns = [
	path('bikes/process-bike-order/<int:pk>/', process_bike_order, name='process-bike-order'),
	path('bikes/order-processed/<int:pk>/', BikeDetailView.as_view(), name='order-processed'),
	path('bikes/<int:pk>/', BikeDetailView.as_view(), name='bike_detail'),
	path('bikes/', BikeListView.as_view(), name='bikes'),
	path('', lambda req: redirect('bikes/')),
]
