from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from . import views

route = DefaultRouter()

urlpatterns = [
    path('login/', obtain_jwt_token),
    # url(r'^authorizations/$', views.UserAuthorizationView.as_view()),
    # url(r'users/(?P<pk>\d+)/password/$', views.PasswordView.as_view()),
]

urlpatterns += route.urls
