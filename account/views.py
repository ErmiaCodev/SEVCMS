from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile
# Create your views here.

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			A = Profile(userid=request.POST['username'], name='', lastname='').save()
			return redirect("/account/login")

	form = UserCreationForm
	return render(request, "registration/register.html", {"form": form})

def edit(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			FR = get_object_or_404(Profile, userid=request.user.username)
			form = ProfileForm(request.POST, request.FILES, instance=FR)
			if form.is_valid():
				c = form.save()
		form = ProfileForm()
		data = list(Profile.objects.filter(userid=request.user.username).values())
		for byte in data:
			data = byte
		return render(request, 'forms/setting.html', {'form': form, 'data': data})
	else:
		return redirect('/account/login')

def get_user(request):
	if request.user.is_authenticated:
		data = list(Profile.objects.filter(userid=request.user.username).values())
		for byte in data:
			data = byte

		return JsonResponse(data)

def panel(request):
	data = list(Profile.objects.filter(userid=request.user.username).values())
	for byte in data:
			data = byte

	return render(request, "forms/sample.html", {"prof": data})

