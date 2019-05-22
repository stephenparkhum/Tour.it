from django.db import models
from .genres import Genres
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.forms import ModelForm


class Artists(models.Model):
    artist_Name = models.CharField(max_length=200)
    artist_Genre = models.CharField(
        max_length=200, choices=Genres.GENRE_CHOICES)
    artist_IG_Username = models.CharField(max_length=200, blank=True)
    artist_FB_URL = models.URLField(default='', blank=True)
    artist_Spotify_URL = models.URLField(default='', blank=True)
    artist_BC_URL = models.URLField(default='', blank=True)
    artist_Show_Count = models.CharField(
        max_length=200, default='0', blank=True)
    owner_ID = models.CharField(
        max_length=200, default="", blank=True)
    signup_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.artist_Name
