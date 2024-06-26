# Generated by Django 5.1 on 2024-04-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_products_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.PositiveIntegerField(default=0, max_length=255, verbose_name='Цена'),
        ),
    ]
