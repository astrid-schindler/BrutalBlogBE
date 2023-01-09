import uuid

from django.db import models

# Create your models here.


class Blogpost(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    id_post = models.CharField(default=uuid.uuid4().hex[:5].upper(), auto_created=uuid.uuid4().hex[:5].upper(), max_length=50, editable=True, unique=True)
    image_url = models.URLField(max_length=500, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
