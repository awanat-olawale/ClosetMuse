from django.db import models
from django.conf import settings
from wardrobe.models import WardrobeItem

class OutfitDeclutter(models.Model):
    DECLUTTER_CHOICES = [
        ("DONATE", "Donate"),
        ("SELL", "Sell"),
        ("DISPOSE", "Dispose")
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="declutters"
    )
    item = models.ForeignKey(
        WardrobeItem,
        on_delete=models.CASCADE,
        related_name="declutters"
    )
    last_worn = models.DateTimeField(blank=True, null=True)
    wear_count = models.IntegerField(blank=True, null=True)
    reason = models.CharField(
        max_length=50,
        choices=DECLUTTER_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.reason}"