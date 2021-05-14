from django.urls import path
from .views import *

urlpatterns = [
	path('', home),
	path('blog/', blog),
	path('blog/post/<slug>', post),
	path('blog/cat/', cat),

]