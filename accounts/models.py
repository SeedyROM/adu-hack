from django.db import models
from core.models import UUIDModel
from django.contrib.auth.models import AbstractUser


class InvalidUserType(BaseException):
    pass


class User(UUIDModel, AbstractUser):
    HOMEOWNER = 0
    CONTRACTOR = 1
    STAFF = 3

    TYPE_CHOICES = (
        (HOMEOWNER, 'Homeowner'),
        (CONTRACTOR, 'Contractor'),
        (STAFF, 'Staff'),
    )

    user_type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICES, default=0)
    contractor_information = models.ForeignKey(
        'accounts.ContractorInformation', blank=True, null=True)
    homeowner_information = models.ForeignKey(
        'accounts.HomeOwnerInformation', blank=True, null=True)

    @property
    def information(self):
        if user_type == HOMEOWNER:
            pass
        elif user_type == CONTRACTOR:
            pass
        elif user_type == STAFF:
            pass
        else:
            raise InvalidUserType()


class HomeOwnerInformation(UUIDModel):
    pass


class ContractorInformation(UUIDModel):
    pass
