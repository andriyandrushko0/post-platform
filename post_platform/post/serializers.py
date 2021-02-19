from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import Post, PostComment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for `post.PostComment` model.
    """
    class Meta:
        model = PostComment
        fields = (
            'id',
            'author_name',
            'content',
            'creation_date',
            'post'
        )
        extra_kwargs = {
            'id': {'read_only': True, 'required': False},
            'post': {'read_only': False, 'required': False}
        }


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for `post.Post` model.
    """
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'link',
            'creation_date',
            'amount_of_upvotes',
            'author_name',
            'comments',
        )
        extra_kwargs = {
            'id': {'required': False},
            'comments': {'required': False}
        }

    def create(self, validated_data):
        """
        Create new `post.Post` instance with or without comments
        :param validated_data:
        :return: post:
        """
        comments_data = validated_data.pop('comments', None)
        post = Post.objects.create(**validated_data)
        if comments_data:
            for comment in comments_data:
                PostComment.objects.create(post=post, **comment)
        return post

    def update(self, instance, validated_data):
        """
        Update post attributes and related comments
        :param instance:
        :param validated_data:
        :return: post:
        """
        comments_data = validated_data.get('comments', None)
        if comments_data:
            for comment in comments_data:
                comment_id = comment.get('id', None)
                if comment_id:
                    try:
                        comment_instance = PostComment.objects.get(id=comment_id)
                        comment_instance.author_name = comment.get('author_name')
                        comment_instance.content = comment.get('content')
                        comment_instance.save()
                    except ObjectDoesNotExist:
                        pass
                else:
                    comment_instance = PostComment(
                        post=instance,
                        author_name=comment.get('author_name'),
                        content=comment.get('content')
                    )
                    comment_instance.save()

        instance.title = validated_data.get('title', instance.title)
        instance.link = validated_data.get('link', instance.link)
        instance.amount_of_upvotes = validated_data.get('amount_of_upvotes', instance.amount_of_upvotes)
        instance.author_name = validated_data.get('author_name', instance.author_name)
        instance.save()
        return instance
