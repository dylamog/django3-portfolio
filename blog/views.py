from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.
def all_blogs(request):
    blogposts = BlogPost.objects.order_by('-date')
    print(blogposts)
    return render(request, 'blog/all_blogs.html', {'blogposts':blogposts})

def detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})