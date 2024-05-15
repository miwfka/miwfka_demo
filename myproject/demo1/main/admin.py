from django.contrib import admin
from .models import *


@admin.register(Status)
class Status_admin(admin.ModelAdmin):
    list_display = ("name", "id")


@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ("name", "price", "id")


@admin.register(Orders)
class Orders_admin(admin.ModelAdmin):
    list_display = ("get_name", "get_email",  "products_id", "qty", "status_id")

    def get_name(self, object):
        return object.user.first_name
    
    get_name.short_description = "ФИО"

    def get_email(self, object):
        return object.user.email
    
    get_email.short_description = "Почта"