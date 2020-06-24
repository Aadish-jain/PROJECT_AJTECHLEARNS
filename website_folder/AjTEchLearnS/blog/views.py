from django.shortcuts import render,HttpResponse
from blog.models import Post

# Create your views here.
def blog(request):
    return render(request,'blog/blog.html')
def blog_page(request):
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request,'blog/blog_page.html',context)
def blogPost(request,slug):
    post = Post.objects.filter(slug = slug).first()
    context = {'post': post}
    # print(post)
    return render(request,'blog/blog_post.html',context) 