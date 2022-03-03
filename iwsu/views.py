# from django.http import HttpResponse

from django.shortcuts import render, redirect
import urllib.request, urllib.parse, urllib.error
import json
import ssl
from diadiem.models import DiaDiem
def home(request):
    danh_sach_dia_diem = DiaDiem.objects.all()
    context = {
        'danh_sach_dia_diem': danh_sach_dia_diem
    }
    return render(request, 'home.html', context)

def diaDiem(request, diadiem_slug):
    try:
       dia_diem_sigle = DiaDiem.objects.get(slug = diadiem_slug)
    except Exception as e:
        raise e
    context = {
        'dia_diem_sigle': dia_diem_sigle,
    }
    return render(request, 'detail.html', context)