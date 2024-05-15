from django.db import models #импорт sql команд (чарфилды и тп)
from django.contrib.auth.models import User #импорт таблицы юзера

class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название") 
    price = models.PositiveIntegerField(max_length=255, default=0, verbose_name="Цена")

    def __str__(self) -> str:
        return str(self.name)
    
    class Meta():
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Status(models.Model):
    name = models.CharField(max_length=255, default='Нfdgdf') #дефолт пишем тк одна строчка в таблице которая не мб пустой и поэтому изначально прописываем дефолт

    def __str__(self) -> str:
        return str(self.name)
    
    class Meta():
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Orders(models.Model):
    address = models.CharField(max_length=255)
    qty = models.PositiveIntegerField(max_length=255, default=1, verbose_name="Количество")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Товар")
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, default=Status, verbose_name="Статус")

    class Meta():
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"


