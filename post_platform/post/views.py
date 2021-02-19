from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from .models import Post, PostComment


class PostAPIView(viewsets.ModelViewSet):
    """
    Api view set for `post.PostComment` model
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentAPIView(viewsets.ModelViewSet):
    """
    Api view set for `post.Post` model
    """
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
