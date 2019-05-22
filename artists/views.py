from django.shortcuts import render
from django.http import HttpResponse
from .models import Artists
from .forms import ArtistForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    full_artist_list = Artists.objects.filter(owner_ID=request.user.id)
    context = {'artist_list': full_artist_list}
    return render(request, 'artists/index.html', context)


def artist_page(request):
    artist_list = Artists.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'artists/index.html', context)


def shows_page(request):
    artist_list = Artists.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'artists/shows.html', context)


def add_show(request):
    full_artist_list = Artists.objects.all()
    context = {'artist_list': full_artist_list}
    return render(request, 'artists/add-show.html', context)


def tours_page(request):
    artist_list = Artists.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'artists/tours.html', context)


def add_tour(request):
    full_artist_list = Artists.objects.all()
    context = {'artist_list': full_artist_list}
    return render(request, 'artists/add-tour.html', context)


# class ArtistListView(request):
#     model = Artists
#     template_name = 'artists/index.html'
#     context_object_name = 'artists_list'
#     artists_list = Artists.objects.filter(owner_ID=request.user.id)
#     ordering = ['-artist_Name']

def artists_list(request):
    full_artist_list = Artists.objects.filter(owner_ID=request.user.id)
    context = {'artist_list': full_artist_list}
    return render(request, 'artists/artist-list.html', context)


def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.owner_ID = request.user.id
            artist.save()
            return render(request, 'artists/index.html')
    else:
        form = ArtistForm()
    return render(request, 'artists/add-artist.html', {'form': form})
