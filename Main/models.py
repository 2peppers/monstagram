import os

from django.contrib.auth.models import User
from django.db import models

from monstagram.settings import UPLOAD_PATH


class Post(models.Model):
    title = models.CharField(max_length=300, default="New Post")
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to=UPLOAD_PATH, blank=True, null=True)
    comment = models.TextField(default='', max_length=2000)
    author = models.ForeignKey(User, related_name='posts')
    added_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def image_path(self):
        if self.image:
            return '%s%s' % (UPLOAD_PATH, os.path.basename(self.image.path))
        return ''

    def __str__(self):
        return "Post {} of {}".format(self.title, self.author.username)

    class Meta:
        ordering = ('-added_at',)

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes')
    post = models.ForeignKey(Post, related_name='likes')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Like for '{}' by '{}'".format(self.post.title, self.user.username)

    class Meta:
        unique_together = ('user', 'post')