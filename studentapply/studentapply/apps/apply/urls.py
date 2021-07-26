from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()

urlpatterns = [
]

urlpatterns += route.urls
