from django.contrib import admin
from flowersapp.models import Buyer


@admin.register(Buyer)
class PlaceAdminModel(admin.ModelAdmin):
    pass
