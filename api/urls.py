from django.urls import path
from .views import *

urlpatterns = [
	path('getuser/', GetUser),
	path('posts/', posts),
	path('avatar/', avatar),
	path('comments/<slug>', comments),
]