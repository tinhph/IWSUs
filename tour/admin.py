from django.contrib import admin
from .models import Tour
# Register your models here.
class TourAdmin(admin.ModelAdmin):
    list_display = ('tour_name','location', 'tour_images', 'begin_date', 'end_date')
    list_display_links = ('tour_name','location')
    list_filter = ('tour_name','description')
    search_fields = ('tour_name','begin_date','end_date')
    list_per_page = 25
admin.site.register(Tour,TourAdmin )
