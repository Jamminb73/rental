from django.db import models
from django.utils import timezone

class ReviewPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField( upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
