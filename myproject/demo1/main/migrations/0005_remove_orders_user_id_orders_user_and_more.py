# Generated by Django 5.1 on 2024-04-29 14:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_orders_options_alter_products_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='user_id',
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status_id',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='main.status'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(default='Новое', max_length=255),
        ),
    ]
