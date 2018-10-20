import uuid
from django.db import models

from core.geocoding import geocode

class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True

class GeoLocationModel(models.Model):
    address = models.CharField(max_width=512)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True

@receiver(post_save, sender=GeoLocationModel)
def save_profile(sender, instance, **kwargs):
    data = geocode(instance.address)
    print(data)