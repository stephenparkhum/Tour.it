from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Tours
from django.forms import ModelForm
from dal import autocomplete
from artists.models import Artists
from django.contrib.auth.models import User


class TourForm(ModelForm):
    class Meta:
        model = Tours
        fields = [
            'artist_Name',
            'tour_Name',
            'tour_Country',
            'tour_Type',
            'start_Date',
            'end_Date',
            'additional_Band'
        ]
