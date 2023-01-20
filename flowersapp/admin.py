from django.contrib import admin
from flowersapp.models import BouquetQuiz, Buyer, BouquetQuiz, Shop
from flowersapp.models import Bouquet, Order
from flowersapp.models import Consultation, Payment


@admin.register(Buyer)
class BuyerAdminModel(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdminModel(admin.ModelAdmin):
    pass


@admin.register(Bouquet)
class BouquetAdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("bouquet_name", )}


@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    pass


@admin.register(Consultation)
class ConsultationAdminModel(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdminModel(admin.ModelAdmin):
    pass

@admin.register(BouquetQuiz)
class BouquetQuizAdminModel(admin.ModelAdmin):
    pass