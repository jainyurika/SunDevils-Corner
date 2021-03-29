from enum import auto
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60, null=False, verbose_name="Title")
    description = models.TextField(max_length=5000, null=True, verbose_name="Description")
    upvotecount = models.IntegerField(default=0, verbose_name="Upvote Count")
    date = models.DateField(auto_now_add=True,verbose_name="Post Created On")

    def __str__(self):
        return self.title

class Comment(models.Model):
    description = models.TextField(max_length=5000, null=True, verbose_name="Description")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
