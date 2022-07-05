from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import Post

# Create your views here.
def main(request):
    return render(request, 'main.html')

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('main')
        
    else:
        form = PostForm
        return render(request, 'write.html', {'form':form})
    
def read(request):
    posts = Post.objects
    return render(request, 'read.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post':post})