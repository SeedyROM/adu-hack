from django.db import models
from core.models import UUIDModel, GeoLocationModel

class Site(UUIDModel, GeoLocationModel):
    pass