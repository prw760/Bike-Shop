from django.db import models


class Frame(models.Model):
	color = models.CharField(max_length=100)
	quantity = models.IntegerField()

	def __str__(self):
		return f"{self.color}"


class Seat(models.Model):
	color = models.CharField(max_length=100)
	quantity = models.IntegerField()

	def __str__(self):
		return f"{self.color}"


class Tire(models.Model):
	type = models.CharField(max_length=100)
	quantity = models.IntegerField()

	def __str__(self):
		return f"{self.type}"


class Basket(models.Model):
	quantity = models.IntegerField()

	def __str__(self):
		return "Standard Basket"


class Bike(models.Model):
	name = models.CharField(max_length=100, default='Generic Bike')
	description = models.CharField(max_length=100)
	frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
	seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
	tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
	basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
	has_basket = models.BooleanField()

	def __str__(self):
		return f"{self.name}"

	@property
	def enough_parts(self):

		bike_id = self.id
		bike = Bike.objects.get(id=bike_id)
		frame = Frame.objects.get(id=bike.frame_id)
		seat = Seat.objects.get(id=bike.seat_id)
		tire = Tire.objects.get(id=bike.tire_id)

		if frame.quantity < 1 or seat.quantity < 1 or tire.quantity < 2:
			return False

		if bike.has_basket:
			basket = Basket.objects.first()
			if basket.quantity < 1:
				return False

		return True


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

	def __str__(self):
		return f"{self.bike.name} order for {self.name} {self.surname}"
