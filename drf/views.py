from time import timezone

from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response

from TaskBlogApp.models import Category, Post, Comment
from drf.serializer import CategorySerializers, PostsSerializers, CommentSerializers, UserSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializers


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class CommentLikeViewSet(viewsets.ViewSet):
    def get(self, request, id=None):
        if id:
            comment = Comment.objects.get(id=id)
            comment.comment_like += 1
            comment.save()
            data = CommentSerializers(Comment.objects.get(pk=id)).data
            content = {'comment': data}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Not Modified."}, status=status.HTTP_304_NOT_MODIFIED)


class CommentDislikeViewSet(viewsets.ViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def get(self, request, id=None):
        if id:
            comment = Comment.objects.get(id=id)
            comment.comment_dislike += 1
            comment.save()
            data = CommentSerializers(Comment.objects.get(pk=id)).data
            content = {'comment': data}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Not Modified."}, status=status.HTTP_304_NOT_MODIFIED)
    #
    # def get(self, request, id=None):
    #     data = CommentSerializers(Comment.objects.get(pk=id)).data
    #     content = {'comment': data}
    #     return Response(content, status=status.HTTP_200_OK)
    #
    # def put(self, request, id=None):
    #     serializer = CommentSerializers(data=request.data)
    #     if serializer.is_valid():
    #         pass
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





