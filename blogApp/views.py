from django.shortcuts import render, HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

def home(request):
    return render(request,'home.html')

# def about(request):
#     return HttpResponse('<h1> Blog About</h1>')

def about(request):
    return render(request,'about.html')
