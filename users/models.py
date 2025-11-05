from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import SET_NULL

from roles.models import Role


class UserModel(AbstractUser):

    username = models.CharField(max_length=150, null=True, blank=True, unique=False)
    email = models.EmailField(unique=True)

    USER_TYPE_CHOICES = (
        ('ADMIN', 'ADMIN'),
        ('EMPLOYEE', 'EMPLOYEE'),
        ('CLIENT', 'CLIENT'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, null=True, blank=True,editable=False)
    phone = models.CharField(max_length=9, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'

    #Crear un username
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)


