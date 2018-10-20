from django.shortcuts import render

from accounts.models import ContractorInformation
from connections.models import Service

def mock_search(request):
    contractors = ContractorInformation.objects.all()
    services = Service.top_5
    
    return render(request, 'connections/search.html', {
        'contractors': contractors,
    })