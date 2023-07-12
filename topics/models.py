from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Topic(models.Model):
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_topic')
    subject = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject