from rest_framework import routers
from .api import PlantViewSet

router=routers.DefaultRouter()

router.register('api/plants',PlantViewSet, 'plants')

urlpatterns = router.urls
