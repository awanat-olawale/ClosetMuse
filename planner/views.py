from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import OutfitPlanner
from .serializers import OutfitPlannerSerializer

class OutfitPlannerViewSet(viewsets.ModelViewSet):
    serializer_class = OutfitPlannerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OutfitPlanner.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        item_ids = serializer.validated_data.pop('item_ids', [])
        planner = serializer.save(owner=self.request.user)
        if item_ids:
            planner.items.set(item_ids)

    def perform_update(self, serializer):
        item_ids = self.request.data.get("item_ids", [])
        planner = serializer.save()
        if item_ids:
            planner.items.set(item_ids)

