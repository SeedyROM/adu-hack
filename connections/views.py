from django.shortcuts import render

from accounts.models import User
from accounts.models import ContractorInformation
from connections.models import Service


def search(request):
    contractors = User.objects.filter(user_type=User.CONTRACTOR)
    popular_services = Service.top_5()

    print(contractors)

    return render(request, 'connections/search.html', {
        'services': popular_services,
        'contractors': contractors,
    })


def searchTwo(request):
    return render(request, 'connections/search2.html')
