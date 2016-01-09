from django.db import models
import datetime
from django.contrib.auth.models import User

class Purchase(models.Model):
	description = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	price = models.DecimalField(max_digits = 4, decimal_places = 2)
	date = models.DateField(default=datetime.date.today)

