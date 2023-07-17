from rest_framework import serializers
from ..models import Topic
from accounts.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer
class TopicSerializer(serializers.ModelSerializer):
    starter = UserSerializer(read_only=True)
    category_name = serializers.CharField(source="get_category_name", read_only=True)
    upvote_count = serializers.IntegerField(source="get_upvote_num", read_only=True)
    downvote_count = serializers.IntegerField(source="get_downvote_count", read_only=True)
    created_data = serializers.DateTimeField(source="get_created_data", read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'starter', 'subject', 'body', 'category', 'category_name', 'users_upvote', 'users_downvote', 'upvote_count', 'downvote_count', 'created_data']

    def create(self, validated_data):
        starter = validated_data.pop('starter')
        subject = validated_data.pop('subject')
        body = validated_data.pop('body')
        category = validated_data.pop('category')
        return Topic.objects.create(starter=starter, subject=subject, body=body, category=category)


    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance