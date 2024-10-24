from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")  

class CustomUserCreationForm(UserCreationForm):
    class Meta:
       model= get_user_model()
       fields= ('email', 'username',) 


class CustomUserChangeForm(UserChangeForm):
    class Meta:
       model= get_user_model()
       fields= ('email', 'username',) 



class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']  # فیلدهای پروفایل که کاربر می‌تواند ویرایش کند
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form__input'}),
            'last_name': forms.TextInput(attrs={'class': 'form__input'}),
            'email': forms.EmailInput(attrs={'class': 'form__input'}),
        }
