from rest_framework import status
from rest_framework.response  import Response
from rest_framework.viewsets import ModelViewSet
from Utils.email import EmailService
from administrators.api.permission import IsAdminOrReadOnly
from administrators.api.serializer import AdminRegisterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from administrators.models import AdminModel

class AdminRegisterView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AdminRegisterSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = AdminModel.objects.all()

    def create(self, request, *args, **kwargs):
        raw_password = request.data.get('password')
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            admin = AdminModel.objects.get(id=response.data['id'])
            EmailService.send_credential_email(
                email=admin.email,
                #username=admin.username,
                password=raw_password,
                first_name=admin.first_name
            )
        return response

    @action(detail=False, methods=['get'], url_path='auth/me/admin')
    def get_current_teacher(self, request):
        serializer = self.get_serializer(request.user.adminmodel)
        return Response(serializer.data)