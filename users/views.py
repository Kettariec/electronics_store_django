from users.forms import UserRegisterForm, UserProfileForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    # получаем объект из запроса, чтобы необязательно было указывать pk:
    def get_object(self, queryset=None):
        return self.request.user
