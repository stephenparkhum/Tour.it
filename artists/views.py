from django.shortcuts import render
from django.http import HttpResponse
from .models import Artists
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



def index(request):
    artist_list = Artists.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'artists/index.html', context)


class ArtistListView(ListView):
    model = Artists
    template_name = 'artists/index.html'
    context_object_name = 'artists_list'
    ordering = ['-artist_Name']


def artist_page(request, artist_id):
    response = "You're looking at the %s artist page"
    return HttpResponse(response, artist_id)


def artists_list(request):
    full_artist_list = Artists.objects.all()
    context = {'artist_list': full_artist_list}
    ordering = ['-artist_Name']
    return render(request, 'artists/artist-list.html', context)


def add_artist(request):
    full_artist_list = Artists.objects.all()
    context = {'artist_list': full_artist_list}
    return render(request, 'artists/add-artist.html', context)


def shows_page(request):
    artist_list = Artists.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'artists/shows.html', context)


def tours_page(request):
    artist_list = Artists.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'artists/tours.html', context)
