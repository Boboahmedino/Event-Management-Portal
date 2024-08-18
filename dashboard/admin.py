from django.contrib import admin
from .models import Profile, Reservation, Category, Room, Breakout, Catering, Venue

# Register your models here.

admin.site.register(Profile)
admin.site.register(Reservation)
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Breakout)
admin.site.register(Catering)
admin.site.register(Venue)