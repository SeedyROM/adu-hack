from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from accounts.models import PropertyOwnerInformation, ContractorInformation

class AccountAdmin(UserAdmin):
    model = get_user_model()

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('property_owner_information', 'contractor_information',)}),
    )

admin.site.register(get_user_model(), AccountAdmin)
admin.site.register(PropertyOwnerInformation)
admin.site.register(ContractorInformation)
