from django.contrib.auth.models import User
from rest_framework import serializers

from TaskBlogApp.models import Category, Post, Comment


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User


class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_post', 'comment_author', 'comment_content', 'comment_like', 'comment_dislike',
                  'comment_createdAt', 'comment_updatedAt')

