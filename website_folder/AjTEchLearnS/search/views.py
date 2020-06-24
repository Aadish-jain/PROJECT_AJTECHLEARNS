from django.shortcuts import render
from blog.models import Post
from django.contrib import messages


# Create your views here.

def search(request):
    query = request.GET['query']
    # allPosts = Post.objects.all()
    if len(query)>100 or len(query) < 1:
        # allPosts = [] or 
        allPosts = Post.objects.none() 

    else:
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostsContent = Post.objects.filter(content__icontains = query)
        allPostsAuthor = Post.objects.filter(author__icontains = query)
        allPoststitle_content = allPostsTitle.union(allPostsContent)
        allPosts = allPoststitle_content.union(allPostsAuthor)
    if allPosts.count() == 0:
        messages.error(request,"No Search Result found.")
    params = {'allPosts' : allPosts,'query':query}
    return render(request,'home/search.html',params)
        # return HttpResponse('This is Search')