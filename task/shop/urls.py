from django.urls import path
from django.shortcuts import redirect
from .views import BikeListView, BikeDetailView


urlpatterns = [
	path('bikes/<int:pk>/', BikeDetailView.as_view(), name='bike_detail'),
	path('bikes/', BikeListView.as_view(), name='bikes'),
	path('', lambda req: redirect('bikes/')),
]
