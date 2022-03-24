from email.policy import default
from sqlite3 import Date
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    moderation = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ('date_posted',)
    
    def __str__(self):
        return f'Post "{self.title}" by {self.author.username}'

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    moderation = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")
        ordering=('date_posted',)
    
    def __str__(self):
        return f'Comment by {self.author.username}'