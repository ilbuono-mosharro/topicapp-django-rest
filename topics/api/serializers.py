from rest_framework import serializers

from ..models import Topic


class TopicSerializer(serializers.ModelSerializer):
    starter = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'starter', 'subject', 'body', 'category', 'users_upvote', 'users_downvote', 'upvote_count', 'downvote_count']

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