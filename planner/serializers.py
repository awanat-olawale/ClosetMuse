from rest_framework import serializers
from .models import OutfitPlanner
from wardrobe.models import WardrobeItem

class WardrobeItemMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardrobeItem
        fields = ["id", "name", "category", "colour"]

class OutfitPlannerSerializer(serializers.ModelSerializer):
    items = WardrobeItemMiniSerializer(many=True, read_only=True)

    class Meta:
        model = OutfitPlanner
        fields = ["id", "owner", "date", "items", "occasion", "notes"]
        read_only_fields = ["owner"]
