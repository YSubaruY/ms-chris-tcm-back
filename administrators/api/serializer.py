from rest_framework import serializers

from administrators.models import AdminModel
from roles.models import Role


class AdminRegisterSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = AdminModel
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone','role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        admin_role = Role.objects.get(name='Admin')
        instance = self.Meta.model(**validated_data)
        instance.role = admin_role
        #instance.is_staff = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance