from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return render(request,'about.html')
    #return HttpResponse('you will make it bhagyashree')

def homepage(request):
    return render(request,'homepage.html')
    #return HttpResponse('hi bhagyashree!! XOXO')
