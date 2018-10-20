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
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username, password)
		if user:
			if user.is_active:
				login(request, user)
			else:
				return HttpResponse("You are not an active user.")
		else:
			return HttpResponse("Invalid login details")
				

def logout(request):
	user_logout(request)

def create_acc(request):
	if request.method == 'POST':
		in_email = request.POST['email']
		in_username = request.POST['username']
		in_password = request.POST['password']
		in_user = User(username=in_username, email=in_email, password=in_password)
		in_user.save()
	return HttpResponse(reverse('accounts:index'))
	
	
@login_required
def update_info(request):
	user = request.user
	if request.method == 'POST':
		pass
	
		
@login_required
def delete_account(request):
	id = request.POST['id']
	del_user = User.objects.get(pk=id)
	del_user.delete()
	return HttpResponse()
	
		
@login_required
def review(request):
	user = request.user
	
