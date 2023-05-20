from rest_framework.routers import DefaultRouter

from .views import UclipViewset

router = DefaultRouter()
router.register(
    prefix="api/v1/uclip", viewset=UclipViewset, basename="Uclip"
)
urlpatterns = router.urls