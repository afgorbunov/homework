from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='аватар')
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True, null=True)

    def avatar_path(self):
        return str(self.avatar)
