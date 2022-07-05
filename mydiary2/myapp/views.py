from django.shortcuts import render, redirect
from .forms import BlogForm
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('index')
        
        else:
            form = BlogForm
            return render(request, 'create.html', {'form':form})