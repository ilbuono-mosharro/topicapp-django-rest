from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter

app_name = "api_categories"

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
urlpatterns = router.urls