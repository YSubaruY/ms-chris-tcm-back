from django.urls import path
from rest_framework.routers import DefaultRouter

from administrators.api.views import AdminRegisterView

router_admin = DefaultRouter()
router_admin.register(prefix='admin', basename='admin', viewset=AdminRegisterView)

