from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import OutfitDeclutter
from .serializers import OutfitDeclutterSerializer

class OutfitDeclutterViewSet(viewsets.ModelViewSet):
    serializer_class = OutfitDeclutterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OutfitDeclutter.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
