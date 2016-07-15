from django.shortcuts import render
from django.views import generic

# Create your views here.
from TaskBlogApp.models import Category, Post


class IndexView(generic.View):
    template_name = 'index.html'

    def get(self, request):
        try:
            categories = Category.objects.all()
            posts = Post.objects.order_by('-post_updatedAd')[:5]
        except Category.DoesNotExist:
            categories = None
        return render(request, 'index.html', {
            'categories': categories,
            'posts': posts})


class PostView(generic.View):
    template_name = 'post.html'

    def get(self, request, pk, id):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            post = None
        return render(request, 'post.html', {
            'post': post})
