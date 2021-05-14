from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import *
from account.models import *
# Create your views here.

def home(request):
	data = Post.objects.filter(status='p').order_by('-publish')
	context = {
		"posts": list(data)[:3]
	}
	return render(request, "home.html", context)

def blog (request):
	data = Post.objects.filter(status='p').order_by('-publish')
	context = {
		"posts": list(data)
	}
	return render(request, "blog.html", context)

def post(request, slug):
	if request.user.is_authenticated:
		if request.method == 'POST':
			A = Comment(author=request.user.username, body=request.POST['body'], slug=slug).save()
			return redirect('/blog/post/' + str(slug))
	post = list(Post.objects.filter(status='p', slug=slug).values())
	if post == []:
		return render(request, "404.html")
	else:
		comments = list(Comment.objects.filter(slug=slug).values())
		for y in comments:
		 	AuthorAV = list(Profile.objects.filter(userid=y['author']).values())[0]['avatar']
		 	y['authorIMG'] = list(Avatar.objects.filter(avatar=AuthorAV).values())[0]['avatarImage']
		for x in post:
			x['comments'] = comments
		return render(request, 'post.html', context={'post': post[0]})



def cat(request):
	return render(request, "cat.html")