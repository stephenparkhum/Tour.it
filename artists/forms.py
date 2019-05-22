from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Artists
from django.utils import timezone
from django.forms import ModelForm


class ArtistForm(ModelForm):
    class Meta:
        model = Artists
        fields = [
            'artist_Name',
            'artist_Genre',
            'artist_IG_Username',
            'artist_FB_URL',
            'artist_Spotify_URL',
            'artist_BC_URL'
        ]
