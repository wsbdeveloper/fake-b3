from django.db import models


class Transactions(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(blank=False, max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name
