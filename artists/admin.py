from django.contrib import admin

# Register your models here.
from .models import Artists as Artist

admin.site.register(Artist)