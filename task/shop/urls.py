from django.urls import path
from django.shortcuts import redirect
from .views import BikeListView


urlpatterns = [
	path('', lambda req: redirect('bikes/') ),
	path('bikes/', BikeListView.as_view(), name='bikes'),
]
