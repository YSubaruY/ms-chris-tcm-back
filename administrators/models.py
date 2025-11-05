from django.db import models

from users.models import UserModel

class AdminModel(UserModel):

    class Meta:
        db_table = 'administrator'

    def __str__(self):
        return f"admin: {self.username}"