# Generated by Django 4.1.5 on 2023-01-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowersapp', '0013_alter_order_bouquet_alter_order_buyer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Действующий заказ'),
        ),
    ]
