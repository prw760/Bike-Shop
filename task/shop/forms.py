from django import forms


class BikeOrderForm(forms.Form):
	name = forms.CharField(max_length=100, label='your name')
	surname = forms.CharField(max_length=100, label='your surname')
	phone_number = forms.CharField(max_length=100, label='your phone number')
	status = forms.CharField(widget=forms.HiddenInput(), label='order status')
