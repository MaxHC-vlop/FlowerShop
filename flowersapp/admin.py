from django.contrib import admin
from django.utils.html import format_html

from flowersapp.models import Bouquet, Order
from flowersapp.models import BouquetQuiz, Buyer, Shop
from flowersapp.models import Consultation, Payment


class OrderItemInline(admin.TabularInline):
    model = Order
    extra = 0


@admin.register(Buyer)
class BuyerAdminModel(admin.ModelAdmin):
    inlines = [OrderItemInline]


@admin.register(Shop)
class ShopAdminModel(admin.ModelAdmin):
    pass


@admin.register(Bouquet)
class BouquetAdminModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("bouquet_name",)}

    readonly_fields = ["bouquet_image", ]

    def bouquet_image(self, bouquet_image):
        return format_html(
            '<img src="/media/{}" height=200px width=auto />', bouquet_image.bouquet_photo
        )

    bouquet_image.short_description = 'Превью букета'


@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    readonly_fields = ["bouquet_image", ]

    def bouquet_image(self, bouquet_image):
        return format_html(
            '<img src="/media/{}" height=200px width=auto />', bouquet_image.bouquet.bouquet_photo
        )

    bouquet_image.short_description = 'Превью букета'



@admin.register(Consultation)
class ConsultationAdminModel(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdminModel(admin.ModelAdmin):
    pass


@admin.register(BouquetQuiz)
class BouquetQuizAdminModel(admin.ModelAdmin):
    pass
