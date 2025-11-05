import os
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response  import Response
from  rest_framework.permissions import IsAuthenticated
from Utils.email import EmailService
from users.api.serializer import UserRegisterSerializer, UserSerializer, UserUpDateSerializer
from users.models import  UserModel
load_dotenv()

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            EmailService.send_credential_email(
                email=user.email,
                username=user.email,
                password=request.data.get('password'),
                first_name=user.first_name
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        user = UserModel.objects.get(id=request.user.id)
        serializer = UserUpDateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)