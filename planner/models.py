from django.db import models
from django.conf import settings
from wardrobe.models import WardrobeItem

class OutfitPlanner(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="outfit_planners"
    )
    date = models.DateField()
    items = models.ManyToManyField(WardrobeItem, related_name="planners")
    occasion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Planner for {self.owner.username} on {self.date}"