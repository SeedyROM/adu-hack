from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def register_property_owner_user(request):
    return render(request, 'accounts/register-owner.html', {})


def register_contractor_user(request):
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
