from django.db import models
from core.models import UUIDModel, GeoLocationModel


class Site(UUIDModel, GeoLocationModel):
    """Work site model, contains geocoded coords and address
    """
    def __str__(self):
        return self.address


class Service(UUIDModel):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()

    @staticmethod
    def top_5():
        return Service.objects.all()[:5]

    def __str__(self):
        return self.name


class Job(UUIDModel):
    completed = models.BooleanField(default=False)

    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    property_owner = models.ForeignKey(
        'accounts.PropertyOwnerInformation',
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    contractor = models.ForeignKey(
        'accounts.ContractorInformation', on_delete=models.CASCADE, blank=True, null=True)
    services = models.ManyToManyField(Service)
    description = models.TextField()


class Review(UUIDModel):
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField()
    contractor = models.OneToOneField(
        'accounts.ContractorInformation', on_delete=models.CASCADE)
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
