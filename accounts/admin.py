from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model= CustomUser
    add_form= CustomUserCreationForm
    form = CustomUserChangeForm
    list_display= UserAdmin.list_display
