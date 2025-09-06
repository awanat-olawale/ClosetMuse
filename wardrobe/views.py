from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import WardrobeItem
from .serializers import WardrobeItemSerializer

class WardrobeItemViewSet(viewsets.ModelViewSet):
    serializer_class = WardrobeItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WardrobeItem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
