from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class WardrobeItem(models.Model):
    CATEGORY_CHOICES = [
        ("TOP", "Top"),
        ("BOTTOM", "Bottom"),
        ("HIJAB", "Hijab"),
        ("SHOES", "Shoes"),
        ("OTHER", "Other")
    ]

    SHOE_CHOICES = [
        ("FLATS", "Flats"),
        ("SANDALS", "Sandals"),
        ("SNEAKERS", "Sneakers"),
        ("BOOTS", "Boots"),
        ('HEELS', "Heels")
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(
        max_length=50,
        choices= SHOE_CHOICES,
        blank= True,
        null= True
    )
    colour = models.CharField(max_length=50)
    fabric_type = models.CharField(max_length=100, blank=True, null =True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= "wardrobe_items"
    )

    def __str__(self):
        return f"{self.name} ({self.category})"
    
    def clean(self):
        #requires subcategory if category is SHOES
        if self.category == "SHOES" and  not self.subcategory:
            raise ValidationError("Subcategory is required if category is SHOES")
        
        #when category isn't SHOES, it prevents subcategory
        if self.category != "SHOES" and self.subcategory:
            raise ValidationError("Subcategory is only allowed when category is SHOES")
