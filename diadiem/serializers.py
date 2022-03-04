import imp
from statistics import mode
from rest_framework import serializers
from .models import DiaDiem

class DiaDiemSerializer(serializers.ModelSerializer):
    class Meta:
        mode= DiaDiem
        fields = ('id', 'ten_dia_diem','thanh_pho','gioi_thieu','ghi_chu' )