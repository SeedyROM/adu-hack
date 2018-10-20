from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from accounts.models import User, PropertyOwnerInformation, ContractorInformation


def register_property_owner_user(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.set_password(request.POST.get('password1'))
        user.user_type = 0

        po = PropertyOwnerInformation()
        po.save()

        user.property_owner_information = po
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'accounts/register-owner.html', {})


def register_contractor_user(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.set_password(request.POST.get('password1'))
        user.user_type = 1
        co = ContractorInformation()
        co.save()

        user.contractor_information = co
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'accounts/register-contractor.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if request.POST.get('next', '/') == '':
            next = '/'
        else:
            next = request.POST.get('next', '/')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
        else:
            return HttpResponse("There was an error with your login information")
    return render(request, 'accounts/login.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {})