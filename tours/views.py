from django.shortcuts import render
from django.http import HttpResponse
from artists.models import Artists
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponseRedirect
from .forms import TourForm
from .models import Tours
from django.contrib.auth.models import User

# Create your views here.


def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.owner_ID = request.user.id
            tour.save()
            return render(request, 'artists/tours.html')
    else:
        form = TourForm()
    return render(request, 'add-tour.html', {'form': form})
