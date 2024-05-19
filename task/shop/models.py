from django.db import models


class Frame(models.Model):
	color = models.CharField(max_length=100)
	quantity = models.IntegerField()


class Seat(models.Model):
	color = models.CharField(max_length=100)
	quantity = models.IntegerField()


class Tire(models.Model):
	type = models.CharField(max_length=100)
	quantity = models.IntegerField()


class Basket(models.Model):
	quantity = models.IntegerField()


class Bike(models.Model):
	name = models.CharField(max_length=100, default='Generic Bike')
	description = models.CharField(max_length=100)
	has_basket = models.BooleanField()
	frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
	seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
	tire = models.ForeignKey(Tire, on_delete=models.CASCADE)


class Order(models.Model):

	PENDING = 'P'
	READY = 'R'
	ORDER_STATUS = [
		(PENDING, 'Pending'),
		(READY, 'Ready'),
	]

	bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)
	status = models.CharField(max_length=100, choices=ORDER_STATUS, default=PENDING)