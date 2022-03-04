from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('localtions', views.DiaDiemView)
urlpatterns = [
  path('diadiem/', include(router.urls))
]