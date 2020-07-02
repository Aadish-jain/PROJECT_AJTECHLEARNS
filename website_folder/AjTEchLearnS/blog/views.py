from django.shortcuts import redirect,render,HttpResponse
from blog.models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def blog(request):
    return render(request,'blog/blog.html')
def blog_page(request):
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request,'blog/blog_page.html',context)
def blogPost(request,slug):
    post = Post.objects.filter(slug = slug).first()
    comments = BlogComment.objects.filter(post = post,parent=None)
    replies = BlogComment.objects.filter(post = post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print(replyDict)
    context = {'post': post , 'comments':comments,'user': request.user,'replyDict':replyDict}
    return render(request,'blog/blog_post.html',context) 

def postComment(request):
    if request.method == "POST":
        user = request.user
        comment = request.POST.get("comment")
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = BlogComment(comment = comment,post = post,user = user)
            comment.save()
            messages.success(request,"Your Comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment = comment,post = post,user = user,parent = parent)

            comment.save()
            messages.success(request,"Your Reply has been posted successfully")
    return redirect(f"/blog/{post.slug}")