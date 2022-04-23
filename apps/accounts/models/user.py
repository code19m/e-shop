from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.accounts.managers.user import CustomUserManager
from apps.utils.mixins import DateTimeMixinModel
from apps.utils.validators import phone_regex


class User(DateTimeMixinModel, AbstractUser):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, blank=True)

    phone_number = models.CharField(max_length=15, blank=True,
                                    validators=(phone_regex,))

    image = models.ImageField(upload_to='photos/%y/%m/%d',
                              null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.role}. {self.first_name} {self.last_name}"
