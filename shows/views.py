from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Shows
from .forms import ShowForm
from artists.models import Artists
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


# def add_show(request):
#     full_artist_list = Artists.objects.all()
#     context = {'artist_list': full_artist_list}
#     return render(request, 'add-show.html', context)


def add_shows(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            show = form.save(commit=False)
            show.owner_ID = request.user.id
            show.save()
            return render(request, 'artists/shows.html')
    else:
        form = ShowForm()
    return render(request, 'add-show.html', {'form': form})
