from dataclasses import fields
from rest_framework import serializers
from .models import Book, Comment


class CommentSerializer(serializers.ModelSerializer):
    comments_owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        # fields = "__all__"
        exclude = ('book',)


class BooksSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
        # fields = ["id", "name", "author", "comments", "definition","createion_date", "updated_date", "published_date"]
