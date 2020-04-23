from django.db import models

# Create your models here.


class Profile(models.Model):
	name = models.CharField(max_length=50)
	mail = models.CharField(max_length=100)
	text = models.CharField(max_length=500)

	def __str__(self):
		return self.name 