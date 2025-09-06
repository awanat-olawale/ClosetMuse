from rest_framework import serializers
from .models import OutfitPlanner
from wardrobe.models import WardrobeItem

class WardrobeItemMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardrobeItem
        fields = ["id", "name", "category", "colour"]

class OutfitPlannerSerializer(serializers.ModelSerializer):
    item_ids = serializers.PrimaryKeyRelatedField(
        queryset=WardrobeItem.objects.all(),
        many=True,
        write_only=True
    )

    items = WardrobeItemMiniSerializer(many=True, read_only=True)

    class Meta:
        model = OutfitPlanner
        fields = ["id", "owner", "date", "items","item_ids", "occasion"]
        read_only_fields = ["owner"]
