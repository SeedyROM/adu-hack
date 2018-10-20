import uuid
from django.db import models

from core.geocoding import get_lat_lng


class UUIDModel(models.Model):
    """An abstract model that uses uuid instead of auto incrementing integers
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class GeocodeError(BaseException):
  pass


class GeoLocationModel(models.Model):
    """An abstract model that stores an address and finds it's coords via geocoding
    """
    address = models.CharField(max_length=512)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            results = get_lat_lng(self.address)
            self.latitude = results['result']['addressMatches'][0]['coordinates']['x']
            self.longitude = results['result']['addressMatches'][0]['coordinates']['y']
        except AttributeError:
            raise GeocodeError('Failed to geocode model!')
        except IndexError:
            print(f'Failed to find latitude/longitude for "{self.address}"')

        # super(GeoLocationModel, self).save()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
