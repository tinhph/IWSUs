from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('details/<slug:diadiem_slug>/', views.diaDiem, name='diaDiem'),
    path('diadiem/', include('diadiem.urls')),
    path('getData_Ajax', views.getData, name = 'getData'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
