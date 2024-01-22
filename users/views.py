from users.forms import UserRegisterForm, UserProfileForm
from django.views.generic import CreateView, UpdateView
from users.models import User
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
import random


class RegisterView(CreateView):
    """Контроллер страницы регистрации"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        code = ''.join(random.sample('0123456789', 5))
        new_user.verify_code = code
        new_user.is_active = False
        send_mail(
            'Верификация',
            f'Перейдите по ссылке для верификации: http://127.0.0.1:8000/users/verification/{code}',
            EMAIL_HOST_USER,
            [new_user.email]
        )
        return super().form_valid(form)
    # def form_valid(self, form):
    #     new_user = form.save()
    #     send_mail(
    #         subject='Вы зарегистрировались!',
    #         message='Добро пожаловать!',
    #         from_email=EMAIL_HOST_USER,
    #         recipient_list=[new_user.email]
    #     )
    #     return super().form_valid(form)


def verification(request, code):
    """Контроллер подтверждения верификации"""
    user = User.objects.get(verify_code=code)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    """Контроллер страницы профиля"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    # получаем объект из запроса, чтобы необязательно было указывать pk:
    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = User.objects.make_random_password()
    request.user.set_password(new_password)
    request.user.save()
    send_mail(
        'Смена пароля',
        f'Ваш новый пароль для авторизации: {new_password}',
        EMAIL_HOST_USER,
        [request.user.email]
    )
    return redirect(reverse('users:login'))
    # new_password = ''.join([str(randint(0, 9)) for i in range(12)])
    # send_mail(
    #     subject='Вы сменили пароль',
    #     message=f'Ваш новый пароль: {new_password}',
    #     from_email=EMAIL_HOST_USER,
    #     recipient_list=[request.user.email]
    # )
    # request.user.set_password(new_password)
    # request.user.save()
    # return redirect(reverse('catalog:home'))
