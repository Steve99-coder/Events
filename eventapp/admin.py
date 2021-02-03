from django.contrib import admin
from .models import Profile,Event,Location
from django.contrib import admin

# Register your models here.

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Location)