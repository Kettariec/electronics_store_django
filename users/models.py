from django.db import models
from django.contrib.auth.models import AbstractUser
import random

random_code = ''.join(random.sample('0123456789', 5))


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    phone = models.CharField(max_length=35, verbose_name="телефон")
    avatar = models.ImageField(upload_to='users/', verbose_name="аватар", null=True, blank=True)
    country = models.CharField(max_length=35, verbose_name="страна", null=True, blank=True)
    verify_code = models.CharField(max_length=5, default=random_code, verbose_name='Код верификации',
                                   null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
