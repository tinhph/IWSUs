# from django.http import HttpResponse

from django.shortcuts import render, redirect
import urllib.request, urllib.parse, urllib.error
import json
import ssl
def home(request):
    
    return render(request, 'home.html')
    # return HttpResponse('Homepages')

def detail(request):
    return render(request, 'detail.html')
    # return HttpResponse('Homepages')