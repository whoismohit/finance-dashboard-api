from rest_framework.routers import DefaultRouter
from .views import RecordViewSet

router = DefaultRouter()
router.register('', RecordViewSet)

urlpatterns = router.urls