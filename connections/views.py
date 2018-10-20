from django.shortcuts import render

from accounts.models import ContractorInformation
from connections.models import Service

def search(request):
    contractors = ContractorInformation.objects.all()
    popular_services = Service.top_5()

    print(popular_services)

    return render(request, 'connections/search.html', {
        'services': popular_services,
        'contractors': contractors,
    })