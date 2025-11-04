from rest_framework.routers import DefaultRouter

from roles.api.views import RolesApiviewSet


router_roles = DefaultRouter()
router_roles.register(prefix='roles', basename='roles', viewset=RolesApiviewSet)