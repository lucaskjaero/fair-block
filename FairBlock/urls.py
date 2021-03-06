"""FairBlock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from Data.views import EmptyViewSet, FullViewSet, HistoryViewSet, ParkingSpotViewSet, StatusViewSet, StateViewSet
from ParkingView.views import index, gallery

router = routers.DefaultRouter()
router.register(r'empty', EmptyViewSet)
router.register(r'full', FullViewSet)
router.register(r'parkingspots', ParkingSpotViewSet)
router.register(r'state', StateViewSet)

urlpatterns = [
    url(r'^$', index),
    url(r'^gallery$', gallery),
    url(r'^api/', include(router.urls)),
    url('^api/history/(?P<spot>.+)/$', HistoryViewSet.as_view({'get': 'list'})),
    url('^api/status/(?P<spot>.+)/$', StatusViewSet.as_view({'get': 'list'})),
    path('admin/', admin.site.urls),
]
