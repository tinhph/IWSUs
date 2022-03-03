from django.db import models
from django.urls import reverse
# Create your models here.
class DiaDiem(models.Model):
    
    ten_dia_diem = models.CharField(max_length=50, unique=True)
    thanh_pho = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    gioi_thieu = models.TextField(max_length=255, blank=True)
    hinh_anh1 = models.ImageField(upload_to='photos/diadiem', blank=True) #365x305
    hinh_anh2 = models.ImageField(upload_to='photos/diadiem', blank=True) #365x305
    hinh_anh3 = models.ImageField(upload_to='photos/diadiem', blank=True) #365x305
    hinh_cover = models.ImageField(upload_to='photos/diadiem', blank=True) #1920x800
    ghi_chu = models.TextField(max_length=255, blank=True)
    def __str__(self):
        return self.ten_dia_diem

    def get_url(self):
        return reverse('diaDiem', args=[self.slug])