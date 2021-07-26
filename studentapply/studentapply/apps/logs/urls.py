from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import LogsViewSet
from . import views

route = DefaultRouter()

route.register('logs', LogsViewSet, basename='logs')

urlpatterns = [
]

urlpatterns += route.urls
