from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'main/home.html')

def single_course(request):
    return render(request, 'main/single_course.html')