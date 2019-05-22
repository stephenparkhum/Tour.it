from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Shows
from django.utils import timezone
from django.forms import ModelForm


class ShowForm(ModelForm):
    class Meta:
        model = Shows
        fields = [
            'artist_Name',
            'venue',
            'venue_Location',
            'show_Date',
            'tour_Selection',
        ]
