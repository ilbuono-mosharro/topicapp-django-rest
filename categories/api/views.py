from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import CategorySerializer
from .permission import IsAdminOrReadOnly
from categories.models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)