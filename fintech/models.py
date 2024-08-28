from django.db import models
from django.core.exceptions import ValidationError


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_total(self):
        currencies = {item.currency for item in self.items.all()}
        if len(currencies) > 1:
            raise ValidationError("Все товары в заказе должны иметь единый тип валюты")
        subtotal = sum(item.price for item in self.items.all())
        discounts = sum(discount.amount for discount in self.discount_set.all())
        taxes = sum(tax.amount for tax in self.tax_set.all())

        self.total_amount = subtotal - discounts + taxes
        self.save()

    def __str__(self):
        return f"Order {self.id}"


class Discount(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Tax(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Taxes'