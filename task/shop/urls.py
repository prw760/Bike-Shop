from django.http import request
from django.urls import path
from django.shortcuts import redirect
from .views import BikeListView, BikeDetailView, process_order, OrderView


urlpatterns = [
	path('bikes/<int:pk>/', BikeDetailView.as_view(), name='bike_detail'),
	path('bikes/', BikeListView.as_view(), name='bikes'),
	path('process-order/', process_order),
	path('order/<int:pk>/', OrderView.as_view(), name='order'),
	path('', lambda req: redirect('bikes/')),
]
