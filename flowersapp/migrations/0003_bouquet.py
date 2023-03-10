# Generated by Django 4.1.5 on 2023-01-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowersapp', '0002_shop_alter_buyer_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bouquet_name', models.CharField(db_index=True, max_length=200, verbose_name='Название букета')),
                ('bouquet_photo', models.ImageField(db_index=True, upload_to='images', verbose_name='Фото букета')),
                ('price', models.FloatField(db_index=True, verbose_name='Цена букета')),
                ('amount', models.IntegerField(db_index=True, verbose_name='Количество букетов в наличии')),
            ],
            options={
                'verbose_name': 'Букет',
                'verbose_name_plural': 'Букеты',
            },
        ),
    ]
