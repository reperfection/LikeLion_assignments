from django.shortcuts import render, redirect
from .forms import DiaryForm
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('index')
        
        else:
            form = DiaryForm
            return render(request, 'create.html', {'form':form})