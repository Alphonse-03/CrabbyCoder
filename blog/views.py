from django.shortcuts import render,redirect
from .models import Post,Comments
from django.contrib import messages
# Create your views here.
def blog(request):
    allBlog=Post.objects.all()
    content={"blogs":allBlog}
    return render(request,"blog/blog.html",content)

def blogpost(request,slug):

    variable=Post.objects.filter(slug=slug).first()
    comments=Comments.objects.all()
    return render(request,"blog/blogpost.html",{'blog':variable,'comments':comments,'user':request.user})

# def comment(request):
#     print("here")
#     if request.method=='POST':
#         comment=request.POST.get('comment')
#         user=request.user
#         postid=request.POST.get('postno')
#         post=Post.objects.get(sno=postid)
#         parentsno=request.POST.get('parentsno')
#         print(comment,user,postid,post.content,parentsno)
#         if parentsno=="":
#             com=Comments(user=user,comment=comment,post=post)
#             com.save()
#             messages.success(request,"comment has been added")
#         else:
#                 parent=Comments.objects.get(sno=parentsno)
#                 com=Comments(user=user,comment=comment,post=post,parent=parent)
#                 com.save()
#                 messages.success(request,"reply has been added")
 
                
            
#     return redirect('/')

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postno")
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get("parentsno")
        if parentSno == "":
            comment= Comments(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"comment added")
        else:
            parent=Comments.objects.get(sno=parentSno)
            comment=Comments(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,"your reply success")

    return redirect(f"/blog/{post.slug}")