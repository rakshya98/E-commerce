from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def index(request):
    blog=BlogPost.objects.all()
    print(blog)
    
    all_posts=[]
    for id in blog:
        all_posts.append(id)
        params={'all_posts':all_posts}
    return render(request,'blog/index.html',params)

def __str__(self):
    return self.title

def blogpost(request,id):
    post=BlogPost.objects.filter(post_id=id)[0] #we need first post so [0]
    print(post)




    return render(request,'blog/blogpost.html',{'post':post})
