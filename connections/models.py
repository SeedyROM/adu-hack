from django.db import models
from core.models import UUIDModel, GeoLocationModel
from accounts.models import PropertyOwnerInformation, ContractorInformation


class Site(UUIDModel, GeoLocationModel):
    def __str__(self):
        return self.address


class Service(UUIDModel):
    name = models.CharField(max_length=256)
    description = models.TextField()


class Job(UUIDModel):
    completed = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    property_owner = models.ForeignKey(PropertyOwnerInformation, on_delete=models.CASCADE)
    contractor = models.ForeignKey(ContractorInformation, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)

