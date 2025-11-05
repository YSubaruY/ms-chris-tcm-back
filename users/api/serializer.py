from rest_framework import serializers
from users.models import UserModel

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'created_at', 'role']

    def validate_email(self, value):
        # Validar que el email sea único
        if UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email ya está registrado.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='role.name')
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'first_name', 'last_name', 'role']

class UserUpDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name']