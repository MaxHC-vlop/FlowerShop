# Generated by Django 4.1.5 on 2023-01-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowersapp', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_index=True, max_length=200, verbose_name='ФИО покупателя')),
                ('phonenumber', models.CharField(db_index=True, max_length=20, verbose_name='Номер телефона владельца')),
            ],
            options={
                'verbose_name': 'Консультация',
                'verbose_name_plural': 'Консультации',
            },
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='bouquet_photo',
            field=models.ImageField(db_index=True, upload_to='media', verbose_name='Фото букета'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='store_photo',
            field=models.ImageField(db_index=True, upload_to='media', verbose_name='Фото магазина'),
        ),
    ]