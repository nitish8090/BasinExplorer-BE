from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('JunctionPoint', views.JunctionPointViewSet, basename='JunctionPoint')
router.register('RiverStream', views.RiverStreamViewSet, basename='RiverStream')
router.register('Watershed', views.WatershedViewSet, basename='Watershed')

urlpatterns = [
    path('', include(router.urls)),
]
