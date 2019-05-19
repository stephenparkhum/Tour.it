from django.db import models

class Genres(models.Model):
    BLACK_METAL = 'Black Metal'
    DEATH_METAL = 'Death Metal'
    DOOM_METAL = 'Doom Metal'
    HARSH_NOISE = 'Harsh Noise Wall'
    ELECTRONIC = 'Electronic'
    SINGER_SONGWRITER = 'Singer-Songwriter'
    GENRE_CHOICES = [
        (BLACK_METAL, 'Black Metal'),
        (DEATH_METAL, 'Death Metal'),
        (DOOM_METAL, 'Doom Metal'),
        (HARSH_NOISE, 'Harsh Noise'),
        (ELECTRONIC, 'Electronic'),
        (SINGER_SONGWRITER, 'Singer-Songwriter')
    ]


