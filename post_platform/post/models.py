from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
