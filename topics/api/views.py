from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import TopicSerializer
from ..models import Topic

class TopicViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing topic.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(starter=self.request.user)


    # user create a topic, user list ther topics, user delete their topic, user update their topics,
    # list all the topics
    # user can vote
    # add a new field public or private