from django.db import models
from django.contrib.auth import get_user_model
from categories.models import Category

User = get_user_model()
# Create your models here.

class Topic(models.Model):
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_topic')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_topic")
    subject = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    users_upvote = models.ManyToManyField(User, related_name="users_upvote", blank=True)
    users_downvote = models.ManyToManyField(User, related_name="users_downvote", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    def upvote_count(self):
        return self.users_upvote.count()

    def downvote_count(self):
        return self.users_downvote.count()

    def created_data(self):
        return self.created_at.strftime("%d %b %Y")