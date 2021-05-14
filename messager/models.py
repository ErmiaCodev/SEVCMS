from django.db import models

# Create your models here.

class Message(models.Model):
	sender = models.CharField(max_length=100)
	to = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	body = models.TextField(max_length=500)

	def __str__(self):
		return self.title

