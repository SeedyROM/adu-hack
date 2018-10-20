from django.contrib import admin

<<<<<<< HEAD
from .models import User, HomeOwnerInformation, ContractorInformation


# Register your models here.
=======
from accounts.models import PropertyOwnerInformation, ContractorInformation

admin.site.register(PropertyOwnerInformation)
admin.site.register(ContractorInformation)
>>>>>>> 40d03a7672ee6a7daa16c3f16d257ed06a48511c
