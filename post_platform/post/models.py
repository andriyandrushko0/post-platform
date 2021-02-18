from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=255)


class PostComment(models.Model):
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
