from django.shortcuts import render, reverse
from .models import User, HomeOwnerInformation, ContractorInformation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout as user_logout

@login_required
def index(request):
	return render(request, 'accounts/index.html', {})

def login(request):
	if request.method == 'POST':
		username = request['username']
		password = request['password']
		authenticate(username, password)
		if user:
			if user.is_active:
				login(request, user)
			else:
				HttpResponse("You are not an active user.")
		else:
			HttpResponse("Invalid login details")
				

def logout(request):
	user_logout(request)

def create_acc(request):
	if request.method == 'POST':
		in_email = request['email']
		in_username = request['username']
		in_password = request['password']
		in_user = User(username=in_username, email=in_email, password=in_password)
		in_user.save()
	return HttpResponse(reverse('accounts:index'))
	
	
def update_info(request):
	user = request.user
	if request.method == 'POST':
		pass
	
		
		
@login_required
def review(request):
	user = request.user
	
	pass
