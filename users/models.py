from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    
    phone = models.CharField(max_length=35, verbose_name='Телефон', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)
    country = models.CharField(max_length=20, verbose_name='Страна', null=True, blank=True)
    is_verified = models.BooleanField(default=False, verbose_name='Верифицирован')
    verification_code = models.CharField(max_length=20, verbose_name='Код верификации', null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
