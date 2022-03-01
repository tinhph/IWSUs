from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Tour(models.Model):
    tour_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True)
    tour_images = models.ImageField(upload_to = 'photos/tours', blank = True)
    num_person = models.IntegerField(blank = True)
    begin_date = models.DateTimeField()
    end_date   = models.DateTimeField()
    location = models.CharField(max_length = 200) 
    epidemic_level = models.IntegerField(blank = True)
    place_recommended = models.CharField(max_length = 200)
    classify = models.CharField(max_length = 100)

    def __str__(self):
        return self.tour_name