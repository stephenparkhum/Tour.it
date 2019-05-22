from django.urls import path
from . import views
from shows import views as show_views
from tours import views as tour_views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/', views.artist_page, name='artist-page'),
    path('list/', views.artists_list, name='artist-list'),
    path('add-artist/', views.add_artist, name='add-artist'),
    path('add-show/', show_views.add_shows, name='add-show'),
    path('shows/', views.shows_page, name='shows-page'),
    path('add-tour/', tour_views.add_tour, name='add-tour'),
    path('tours/', views.tours_page, name='tours-page'),
]
