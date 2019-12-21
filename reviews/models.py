from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

User = settings.AUTH_USER_MODEL

class ReviewPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField( upload_to='images/', null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

class Comment(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __str__(self):
        return self.title
