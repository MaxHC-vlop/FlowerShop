from django.contrib import admin
from flowersapp.models import Buyer, Shop
from flowersapp.models import Bouquet


@admin.register(Buyer)
class BuyerAdminModel(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdminModel(admin.ModelAdmin):
    pass


@admin.register(Bouquet)
class BouquetAdminModel(admin.ModelAdmin):
    pass
