# from msilib.schema import MoveFile
from rest_framework import serializers

from .models import Post, Comment


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        # apply filter on data
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        # get tree representation of the field
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PostListSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'author', 'date_posted')


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    children = RecursiveField(many=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        # retreive only comments without parents
        list_serializer_class = FilterReviewListSerializer
        model = Comment
        fields = ('id', 'content', 'author', 'children', 'parent')


class PostDetailSerializer(serializers.ModelSerializer):

    # get author's username instead of id
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    feed_comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        exclude = ('moderation',)
