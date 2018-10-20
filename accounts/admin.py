from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from accounts import models

class AccountAdmin(UserAdmin):
    """Adds custom fields to the admin panel interface
    """
    model = get_user_model()

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('user_type', 'property_owner_information', 'contractor_information',)}),
    )

admin.site.register(get_user_model(), AccountAdmin)
admin.site.register(models.PropertyOwnerInformation)
admin.site.register(models.ContractorInformation)
