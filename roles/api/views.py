from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from roles.api.permissions import IsAdminOrReadOnly
from roles.api.serializers import RolesSerializer
from roles.models import Role


class RolesApiviewSet(ModelViewSet):
    permission_classes =[IsAdminOrReadOnly]
    serializer_class = RolesSerializer
    queryset = Role.objects.all()
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['name']