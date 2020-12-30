from django.contrib import admin
from .models import *

class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin","destination","duration",)

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flight",)

admin.site.register(flights,FlightAdmin)
admin.site.register(airport)
admin.site.register(passenger,PassengerAdmin)
# Register your models here.
