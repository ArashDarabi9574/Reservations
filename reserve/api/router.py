from rest_framework import routers
from django.urls import path, include
from reserve.api import viewset

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
]
