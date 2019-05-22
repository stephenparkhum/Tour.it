from django.db import models
from django.shortcuts import render
from artists.models import Artists

# Create your models here.


def artist_avail_list(request):
    artist_list = []
    user_artist_list = Artists.objects.filter(id=request.user.id)
    for artist in user_artist_list:
        artist_list.append(artist)
    context = artist_list
    return render(request, 'artists-add-show.html', context)


# def add_show(request):
#     full_artist_list = Artists.objects.filter(id=request.user.id)
#     context = {'artist_list': full_artist_list}
#     return render(request, 'artists/add-show.html', context)


# class TEST_LIST(models.Model):
#     BLACK_METAL = 'Black Metal'
#     DEATH_METAL = 'Death Metal'
#     DOOM_METAL = 'Doom Metal'
#     HARSH_NOISE = 'Harsh Noise Wall'
#     ELECTRONIC = 'Electronic'
#     SINGER_SONGWRITER = 'Singer-Songwriter'
#     GENRE_CHOICES = [
#         (BLACK_METAL, 'Black Metal'),
#         (DEATH_METAL, 'Death Metal'),
#         (DOOM_METAL, 'Doom Metal'),
#         (HARSH_NOISE, 'Harsh Noise'),
#         (ELECTRONIC, 'Electronic'),
#         (SINGER_SONGWRITER, 'Singer-Songwriter')
#     ]


class Shows(models.Model):
    artist_Name = models.CharField(max_length=200)
    venue = models.CharField(max_length=200, blank=True)
    venue_Location = models.CharField(max_length=200, blank=True)
    show_Date = models.DateField(default='', blank=True)
    tour_Selection = models.CharField(max_length=200, default='', blank=True)
    owner_ID = models.CharField(
        max_length=200, default="", blank=True)

    def __str__(self):
        return self.artist_Name
