from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.
def main(request):
    return render(request, 'main.html')

def write(request):
    return render(request, 'write.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.pub_date = timezone.now()
    blog.writer = request.POST['writer']
    blog.feeling = request.POST['feeling']
    blog.body = request.POST['body']
    blog.image = request.FILES.get('image')
    blog.save()
    return redirect('read')

def read(request):
    blogs = Blog.objects
    return render(request, 'read.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, id = id)
    return render(request, 'detail.html', {'blog':blog})

def edit(request, id):
    edit_blog = Blog.objects.get(id = id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.pub_date = timezone.now()
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.image = request.FILES.get('image')
    update_blog.save()
    return redirect('detail', id)

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('read')