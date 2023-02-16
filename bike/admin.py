from django.contrib import admin
from .models import *

# Register your models here.

class PaymentInline(admin.StackedInline):
    model=Payment
    

class ExtraInline(admin.StackedInline):
    model=Extra
    

class StationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                   {'fields': ['name']}),
        ('Bushines information', {'fields': ['free_bikes', 'empty_slots'], 'classes': ['collapse']}),
        ('Location',             {'fields': ['latitude', 'longitude'], 'classes': ['collapse']}),
        ('Date information',     {'fields': ['timestamp'], 'classes': ['collapse']}),
    ]

    inlines = [ExtraInline, PaymentInline]

admin.site.register(Station, StationAdmin)