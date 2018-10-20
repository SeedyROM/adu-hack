from django.db import models
from core.models import UUIDModel
from django.contrib.auth.models import AbstractUser


class InvalidUserType(BaseException):
    """Handle invalid user_type value
    """
    pass


class User(UUIDModel, AbstractUser):
    PROPERTY_OWNER = 0
    CONTRACTOR = 1
    STAFF = 2

    TYPE_CHOICES = (
        (PROPERTY_OWNER, 'Property Owner'),
        (CONTRACTOR, 'Contractor'),
        (STAFF, 'Staff'),
    )

    user_type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICES, default=0
    )
    contractor_information = models.ForeignKey(
        'accounts.ContractorInformation',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='user',
    )
    property_owner_information = models.ForeignKey(
        'accounts.PropertyOwnerInformation',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='user',
    )

    @property
    def information(self):
        """Determine which information should be returned to the user
        """
        if user_type == self.PROPERTY_OWNER:
            return self.property_owner_information
        elif user_type == self.CONTRACTOR:
            return self.contractor_information
        elif user_type == self.STAFF:
            return self
        else:
            raise InvalidUserType('Invalid user type!')


class PropertyOwnerInformation(UUIDModel):
    reviews = models.ManyToManyField('connections.Review', blank=True)

    def __str__(self):
        return f'{self.user.username}\'s information'

    class Meta:
        verbose_name = 'Property Owner'
        verbose_name_plural = 'Property Owners'


class ContractorInformation(UUIDModel):
    services = models.ManyToManyField('connections.Service')
    reviews = models.ManyToManyField('connections.Review', blank=True)

    class Meta:
        verbose_name = 'Contractor'
        verbose_name_plural = 'Contractors'
