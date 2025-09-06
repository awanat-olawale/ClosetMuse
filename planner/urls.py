from rest_framework.routers import DefaultRouter
from .views import OutfitPlannerViewSet

router = DefaultRouter()
router.register(r'planner', OutfitPlannerViewSet, basename='planner')

urlpatterns = router.urls
