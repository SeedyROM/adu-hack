import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.geocoding import geocode


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class GeocodeError(BaseException):
  pass

class GeoLocationModel(models.Model):
    address = models.CharField(max_length=512)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self):
        try:
            results = geocode(self.address)
            self.latitude = results[0]["geometry"]["location"]["lat"]
            self.longitude = results[0]["geometry"]["location"]["lng"]
        except AttributeError:
            raise GeocodeError('Failed to geocode model!')
        except IndexError:
            print(f'Failed to find latitude/longitude for "{self.address}"')

        super(GeoLocationModel, self).save()

    class Meta:
        abstract = True
