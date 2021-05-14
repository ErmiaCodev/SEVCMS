from django.shortcuts import render
from django.http import JsonResponse
from app.models import *
from account.models import *
# Create your views here.

def GetUser(request):
	if request.user.is_authenticated:
		data = list(Profile.objects.filter(userid=request.user.username).values())
		for byte in data:
			data = byte

		return JsonResponse(data)


def posts(request):
	data = Post.objects.filter(status='p').order_by('-publish').values()
	context = {
		"posts": list(data)
	}
	print(context['posts'][0])
	return JsonResponse(context)

def avatar(request):
	data = Avatar.objects.all().values()
	context = {
		"avatars": list(data)
	}
	return JsonResponse(context)


def comments(request, slug):
	data = list(Comment.objects.filter(slug=slug).values())
	return JsonResponse({"data": data})
	