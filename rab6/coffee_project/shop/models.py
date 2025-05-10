from django.db import models

class Coffee(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f"{self.name} — {self.price}₽"