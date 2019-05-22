from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/', views.artist_page, name='artist-page'),
    path('list/', views.artists_list, name='artist-list'),
    path('add-artist/', views.add_artist, name='add-artist'),
    path('add-show/', views.add_show, name='add-show'),
    path('shows/', views.shows_page, name='shows-page'),
    path('add-tour/', views.add_tour, name='add-tour'),
    path('tours/', views.tours_page, name='tours-page'),


]
