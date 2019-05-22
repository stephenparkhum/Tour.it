from django.db import models
from django.shortcuts import render
from artists.models import Artists

# Create your models here.
def add_show(request):
    full_artist_list = Artists.objects.all()
    context = {'artist_list': full_artist_list}
    return render(request, 'artists/add-show.html', context)
