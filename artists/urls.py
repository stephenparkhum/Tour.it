from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/', views.artist_page, name='artist-page'),
    path('artist/list/', views.artists_list, name='artist-list'),
    path('artist/add-artist/', views.add_artist, name='add-artist'),
    path('shows/', views.shows_page, name='shows-page'),
    path('tours/', views.tours_page, name='tours-page'),
    

]
