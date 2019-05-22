from django.urls import path
from . import views

urlpattersns = [
    path('artists/add-show/', views.add_shows, name='add-show'),
]
