# Generated by Django 5.1 on 2024-05-11 17:19

import django.db.models.deletion
import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_orders_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='products_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='qty',
            field=models.PositiveIntegerField(default=1, max_length=255, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status_id',
            field=models.ForeignKey(default=main.models.Status, on_delete=django.db.models.deletion.CASCADE, to='main.status', verbose_name='Статус'),
        ),
    ]