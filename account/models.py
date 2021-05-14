from django.db import models

# Create your models here.

class Profile(models.Model):
	userid = models.CharField(max_length=100)
	name = models.CharField(max_length=100, default=None)
	lastname = models.CharField(max_length=100)
	avatar = models.CharField(max_length=200)

	def __str__(self):
		return self.userid