from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    """Форма для регистрации"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    """Форма для профиля пользователя"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        del self.fields['password']
