from django.urls import path
from . import views

urlpattersns = [
    path('artists/add-tour/', views.add_tour, name='add-tour'),
]
