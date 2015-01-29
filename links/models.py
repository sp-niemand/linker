from django.db import models
from django.contrib.auth.models import User

LINK_MAX_LENGTH = 2048
TAG_MAX_LENGTH = 64

class LinkTag(models.Model):
    name = models.CharField(max_length=TAG_MAX_LENGTH)

class Link(models.Model):
    author = models.ForeignKey(User)
    link = models.URLField(max_length=LINK_MAX_LENGTH)
    description = models.TextField()
    created_when = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(LinkTag)