from django.contrib import admin

from accounts.models import PropertyOwnerInformation, ContractorInformation

admin.site.register(PropertyOwnerInformation)
admin.site.register(ContractorInformation)
