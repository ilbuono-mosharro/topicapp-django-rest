from rest_framework import serializers
from accounts.api.serializers import UserSerializer
from ..models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['created_at', 'updated_at']