from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.views import View
from .models import Post
from .forms import CommentForm
# Create your views here.

all_posts = []

class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = 'posts'
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
        
# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/index.html",{
#         "posts":latest_posts
#         })


# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts":all_posts
#     })
    
class PostListView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = 'all_posts'


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id") 
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("detail-post", args=[slug]))
        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)
            
        
    
    

# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tag.all()
#     })
