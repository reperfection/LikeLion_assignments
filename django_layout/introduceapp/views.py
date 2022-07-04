from django.shortcuts import render

# Create your views here.
def layout(request):
    return render(request, 'layout.html')

def main(request):
    return render(request, 'main.html')

def department(request):
    return render(request, 'department.html')

def grid(request):
    return render(request, 'grid.html')

def html_css(request):
    return render(request, 'html_css.html')

def timetable(request):
    return render(request, 'timetable.html')