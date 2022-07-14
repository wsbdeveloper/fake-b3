import uuid
from django.db import models
from django.utils.timezone import now


class Simulations(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    simulation_id = models.UUIDField(default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    amount = models.IntegerField(blank=False, default=0,)
    deadline = models.IntegerField(blank=False, default=0)
    ipca = models.FloatField(
        blank=True,
        default=0
    )
    cdi = models.FloatField(
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
        return self.name
