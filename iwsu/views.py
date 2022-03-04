# from django.http import HttpResponse

from django.http import JsonResponse
from django.shortcuts import render, redirect
import urllib.request, urllib.parse, urllib.error
import json
import ssl
from diadiem import serializers
from diadiem.models import DiaDiem
import urllib.request, urllib.parse, urllib.error
import json
import ssl

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

#lấy data bằng ajax
def getData(request):
    if request.method == 'GET':
        api_key = False
    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        local = request.GET['local_views']
        address = local
        if len(address) < 1: break

        parms = dict()
        parms['address'] = address
        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        print(json.dumps(js, indent=4))

        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        print('lat', lat, 'lng', lng)
        location = js['results'][0]['formatted_address']

        data_check = {
            'lat_key': lat,
            'lng_key':lng
        }

        return JsonResponse(data_check)
    else:
        return JsonResponse("Error")
