from rest_framework import serializers
from .models import OutfitDeclutter

from rest_framework import serializers
from .models import OutfitDeclutter
from wardrobe.models import WardrobeItem

class WardrobeItemMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardrobeItem
        fields = ["id", "name", "category", "colour"]

class OutfitDeclutterSerializer(serializers.ModelSerializer):
    item = WardrobeItemMiniSerializer(read_only=True)

    class Meta:
        model = OutfitDeclutter
        fields = [
            "id", "owner", "item", "last_worn",
            "wear_count", "reason", "created_at"
        ]
        read_only_fields = ["owner", "created_at"]
