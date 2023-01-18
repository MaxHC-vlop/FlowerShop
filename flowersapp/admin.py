from django.contrib import admin
from flowersapp.models import Buyer, Shop


@admin.register(Buyer)
class BuyerAdminModel(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdminModel(admin.ModelAdmin):
    pass
