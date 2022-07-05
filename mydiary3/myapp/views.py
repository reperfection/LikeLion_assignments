from django.shortcuts import render, redirect, get_object_or_404
from .forms import DiaryForm
from django.utils import timezone
from .models import Diary

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
    
def read(request):
    diarys = Diary.objects
    return render(request, 'read.html', {'diarys': diarys})

def detail(request, id):
    diary = get_object_or_404(Diary, id=id)
    return render(request, 'detail.html', {'diary':diary})