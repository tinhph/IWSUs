# from django.http import HttpResponse

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Homepages')

def detail(request):
    return render(request, 'detail.html')
    # return HttpResponse('Homepages')