from .views import TopicViewSet
from rest_framework.routers import DefaultRouter

app_name = "api_topics"

router = DefaultRouter()
router.register(r'topics', TopicViewSet, basename='topics')
urlpatterns = router.urls
