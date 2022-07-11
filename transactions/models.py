from django.db import models
from django.utils.timezone import now


class Transactions(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    ipca = models.FloatField(
        blank=True,
        default=0
    )
    rate = models.FloatField(
        blank=True,
        default=0
    )
    irr = models.FloatField(
        blank=True,
        default=0
    )

    def __str__(self) -> str:
        return f'name: $name - amount: $amount - ipca: $ipca - rate: $rate - irr: $irr'
