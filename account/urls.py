from django.urls import path
from .views import *

urlpatterns = [
	path('register/', register),
	path('profile/', edit),
	path('panel/', panel)
]