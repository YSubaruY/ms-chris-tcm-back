from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from administrators.models import AdminModel

@admin.register(AdminModel)
class DirectorModel(BaseUserAdmin):
    pass