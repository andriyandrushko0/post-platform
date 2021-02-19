from django.db import models


class PostComment(models.Model):
    """
    Stores a single comment entry, related to :model `post.Post`.

    # Create comment:
    >>> comment = PostComment(post=post_instance, author_name="Andriy", content="My comment")
    >>> comment.save()
    """
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=511)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Post(models.Model):
    """
    Stores a single post entry.

    # Create post:
    >>> post = Post(title="My post title", link="http:\\google.com", amount_of_upvotes=10, author_name="Andriy")
    >>> post.save()
    """
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title
