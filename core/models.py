import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.geocoding import geocode


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class GeoLocationModel(models.Model):
    address = models.CharField(max_length=512)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True


@receiver(post_save, sender=GeoLocationModel)
def save_profile(sender, instance, **kwargs):
    data = geocode(instance.address)
    print(data)
