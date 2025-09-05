from rest_framework import serializers
from .models import WardrobeItem

class WardrobeItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = WardrobeItem
        fields = ["id", "name", "category", "subcategory","colour", "fabric_type", "owner"]
        read_only_fields = ["id", "owner"]

    def validate(self, data):
        category = data.get("category", getattr(self.instance, "category", None))
        subcategory = data.get("subcategory", getattr(self.instance, "subcategory", None))

        if category == "SHOES" and not subcategory:
            raise serializers.ValidationError(
                {"subcategory": "Subcategory is required when category is SHOES."}
            )
        if category != "SHOES" and subcategory:
            raise serializers.ValidationError(
                {"subcategory": "Subcategory is only allowed when category is SHOES."}
            )
        return data