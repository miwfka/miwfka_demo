from django.db import models
from django.contrib.auth.models import User

class Cars(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тачила", default="abcd")
    
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta():
        verbose_name = "Тачки"
        verbose_name_plural = "Тачка"

class Status(models.Model):
    name = models.CharField(max_length=255, default='1') 

    def __str__(self) -> str:
        return str(self.name)
    
    class Meta():
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(verbose_name="Дата бронирования")
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, verbose_name="Тачка")
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус", default=1)

    class Meta():
        verbose_name = "Заявки"
        verbose_name_plural = "Заявка"

