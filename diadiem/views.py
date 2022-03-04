from django.shortcuts import render
from html5lib import serialize
from matplotlib.pyplot import cla
from rest_framework import viewsets

from .models import DiaDiem
from .serializers import DiaDiemSerializer

# Create your views here.

class DiaDiemView(viewsets.ModelViewSet):
    queryset = DiaDiem.objects.all()
    serialize_class = DiaDiemSerializer
