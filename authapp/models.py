from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomerUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    avatar = models.ImageField(upload_to='users_avatars', verbose_name='аватар', blank=True)
    about = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    patronymic = models.CharField(verbose_name='отчество', max_length=128, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)