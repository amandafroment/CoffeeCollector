from django.contrib import admin
from .models import Coffee, Location, Rating

# Register your models here.

admin.site.register(Coffee)
admin.site.register(Location)
admin.site.register(Rating)