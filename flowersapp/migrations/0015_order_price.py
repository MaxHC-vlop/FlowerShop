# Generated by Django 4.1.5 on 2023-01-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowersapp', '0014_order_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(db_index=True, null=True, verbose_name='Стоимость заказа'),
        ),
    ]
