from django.shortcuts import render, redirect, HttpResponse
from .models import *

def home(request):
    if request.method == "GET":
        context = {"posts" : Post.objects.all()}
        return render(request, "index.html", context)
    else:
        return HttpResponse("Operation not allowed")
    
def add(request):
    if request.method == "GET":
        return render(request, "add.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
      
        # create the Post instance then save to db
        new_post = Post(title=title, content=content)  
        new_post.save()
        
        return redirect("/show/"+ str(new_post.id))
    else:
        return HttpResponse("Operation not allowed")

def show(request, id):
    if request.method == "GET":
        context = {"post": Post.objects.get(id=id)}
        return render(request, "show.html", context)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("/")

def edit(request, id):
    if request.method == "GET":
        context = {"post": Post.objects.get(id=id)}
        return render(request, "add.html", context)
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        # update the Post instance then save to db
        post = Post.objects.get(id=id) 
        post.title = title
        post.content = content
        post.save()
        return redirect("/show/"+ str(post.id))
    else:
        return HttpResponse("Operation not allowed")


    
