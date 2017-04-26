from django.conf.urls import include, url
from django.contrib import admin

from .views import captureEvents

urlpatterns = [
    url(r'^',captureEvents,name="capturer"),
]
