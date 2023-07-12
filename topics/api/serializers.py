from rest_framework import serializers
from ..models import Topic

class TopicSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['subject', 'body', 'category', 'upvote', 'downvote']