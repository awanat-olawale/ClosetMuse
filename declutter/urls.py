from rest_framework.routers import DefaultRouter
from .views import OutfitDeclutterViewSet

router = DefaultRouter()
router.register(r'declutter', OutfitDeclutterViewSet, basename='declutter')

urlpatterns = router.urls
