from django.db import models
from django.utils import timezone
from tinymce import models as tn
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	STATUS_CHOICES = (
		('d', 'Draft'),
		('p', 'Published'),
	)
	CAT_CHOICES = (
		('Gaming', "Game"),
		('devel', 'Development'),
		('art', 'Arts'),
	)
	USERS = (
		('ermia', 'Ermia'),
		('sareha', 'Sareha'),
		('Anonymous', 'Ghost'),
	)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=100, unique=True)
	description = models.TextField()
	body_text = tn.HTMLField()
	thumbnail = models.ImageField(upload_to='images')
	cat = models.CharField(max_length=255, choices=CAT_CHOICES, default=None)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=100, choices=USERS)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

	def __str__(self):
		return self.title


class Avatar(models.Model):
	avatar = models.CharField(max_length=200, unique=True)
	avatarImage = models.ImageField(upload_to='avatars')

	def __str__(self):
		return self.avatar

class Comment(models.Model):
	author = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	body = models.TextField(max_length=900)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s... by %s ' % (self.body[:10], self.author)

		