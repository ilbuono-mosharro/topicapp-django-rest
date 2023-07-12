from rest_framework import viewsets
from .serializers import TopicSerializer
from ..models import Topic

class TopicViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing topic.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(starter=self.request.user)