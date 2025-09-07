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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)