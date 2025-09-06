from django.contrib import admin
from django.contrib import admin
from .models import OutfitPlanner

@admin.register(OutfitPlanner)
class OutfitPlannerAdmin(admin.ModelAdmin):
    list_display = ("owner", "date", "occasion")

