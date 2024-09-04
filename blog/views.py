from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import *

def hello_blog(request):
    return HttpResponse("Hello, Blog!")


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})