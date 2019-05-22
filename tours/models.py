from django.db import models
from .tour_types import TourType
from artists.models import Artists
from itertools import repeat
# Create your models here.


class Tours(models.Model):
    artist_Name = models.CharField(max_length=200)
    tour_Name = models.CharField(max_length=200, blank=True)
    tour_Country = models.URLField(default='', blank=True)
    tour_Type = models.CharField(max_length=200, choices=TourType.TOUR_TYPES)
    start_Date = models.DateField(default='', blank=True)
    end_Date = models.DateField(default='', blank=True)
    additional_Band = models.CharField(max_length=200)
    owner_ID = models.CharField(
        max_length=200, default="", blank=True)

    def __str__(self):
        return self.artist_Name
