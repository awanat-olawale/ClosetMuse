from rest_framework.routers import DefaultRouter
from .views import WardrobeItemViewSet

router = DefaultRouter()
router.register(r'wardrobe', WardrobeItemViewSet, basename='wardrobe')

urlpatterns = router.urls
