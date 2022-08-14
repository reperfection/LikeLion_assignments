from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, HashtagForm
from django.utils import timezone
from .models import Post, Comment, Hashtag
from django.http import request

# Create your views here.
def main(request):
    return render(request, 'main.html')

def write(request, post = None):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            form.save_m2m()
            return redirect('main')
        
    else:
        form = PostForm (instance = post)
        return render(request, 'write.html', {'form':form})
    
def read(request):
    posts = Post.objects
    return render(request, 'read.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST" :
        form = CommentForm(request.POST)
        if form.is_valid() :
            comment = form.save(commit = False)
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail', id)
    else:
        form = CommentForm()
        return render(request, 'detail.html', {'post':post, 'form':form})

def edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('read')
        
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('read')

def hashtag(request, hashtag=None) :
    if request.method == 'POST' :
        form = HashtagForm(request.POST, instance = hashtag)
        if form.is_valid() :
            hashtag = form.save(commit = False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']) :
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다"
                return render(request, 'hashtag.html', {'form':form, "error_message":error_message})
            else :
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('read')
    else :
        form = HashtagForm(instance = hashtag)
        return render(request, 'hashtag.html', {'form':form})