from django.db import models


class Buyer(models.Model):
    full_name = models.CharField(
        'ФИО покупателя',
        max_length=200,
        db_index=True
    )
    address = models.TextField(
        'Адрес квартиры',
        db_index=True
    )
    email = models.EmailField(
        'Почта покупателя',
        db_index=True
    )
    phonenumber = models.CharField(
        'Номер телефона владельца',
        max_length=20,
        db_index=True
    )

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Shop(models.Model):
    shop_name = models.CharField(
        'Название магазина',
        max_length=200,
        db_index=True
    )
    store_photo = models.ImageField(
        'Фото магазина',
        upload_to='images',
        db_index=True
    )
    address = models.TextField(
        'Адрес Магазина',
        db_index=True
    )
    is_working = models.BooleanField(
        'Работает ли магазин',
        db_index=True
    )

    def __str__(self) -> str:
        return self.shop_name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
