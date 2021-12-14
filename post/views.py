from django.db.models import fields
from django.forms.models import ModelForm
from django.shortcuts import render
from django.forms import ModelForm
from post.models import Post
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    temp = Post.objects.all()
    return render(request,'index.html' , {"posts":temp})


def newPost(request):
    if request.method == "POST":
        newpost = Post()
        newpost.title = request.POST["title"]
        newpost.body = request.POST["body"]
        newpost.save()
        return HttpResponseRedirect(reverse('index'))


    return render(request,'newPost.html',{"form":PostForm()})

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','body']


