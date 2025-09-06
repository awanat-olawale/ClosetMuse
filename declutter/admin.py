from django.contrib import admin
from django.contrib import admin
from .models import OutfitDeclutter

@admin.register(OutfitDeclutter)
class OutfitDeclutterAdmin(admin.ModelAdmin):
    list_display = ("owner", "item_id", "last_worn", "wear_count", "reason")

