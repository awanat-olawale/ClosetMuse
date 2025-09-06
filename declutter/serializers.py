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
    #POST items
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=WardrobeItem.objects.all(),
        write_only=True
    )
    #For GET, show nested items
    item = WardrobeItemMiniSerializer(read_only=True)

    class Meta:
        model = OutfitDeclutter
        fields = [
            "id", "owner", "item", "item_id", "last_worn",
            "wear_count", "reason", "created_at"
        ]
        read_only_fields = ["owner", "created_at"]

    def create(self, validated_data):
        item_instance = validated_data.pop("item_id")
        return OutfitDeclutter.objects.create(item=item_instance, **validated_data)
