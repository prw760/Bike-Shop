from django.http import request
from django.urls import path
from django.shortcuts import redirect
from .views import BikeListView, BikeDetailView, OrderView, process_bike_order


urlpatterns = [
	path('process-order/', process_bike_order(request), name='process-order'),
	path('order/<int:pk>/', OrderView.as_view(), name='order'),
	path('bikes/<int:pk>/', BikeDetailView.as_view(), name='bike_detail'),
	path('bikes/', BikeListView.as_view(), name='bikes'),
	path('', lambda req: redirect('bikes/')),
]
