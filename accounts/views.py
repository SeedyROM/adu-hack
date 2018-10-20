from django.shortcuts import render
from .models import User, HomeOwnerInformation, ContractorInformation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse

@login_required
def index(request):
	return render(request, 'accounts/index.html', {})

def login(request):
	if request.method == 'POST':
		get_object_or_404(username=request['username'])
		if request.

def logout(request):
	logout(request)

def create_acc(request):
	if 
	
	
# Create your views here.
def index(request):
    pass

def login(request):
    pass

def logout(request):
    pass

def create_acc(request):
    pass

def update_info(request):
    pass

def review(request):
    pass
