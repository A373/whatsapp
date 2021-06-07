from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    phone = models.BigIntegerField(unique=True, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name_plural = 'users'


class chats(models.Model):
     user_name = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
     message = models.TextField(max_length=255, null=True, blank=True)
     created = models.DateTimeField()



class status(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField()
    created = models.DateTimeField()


class groups(models.Model):
     username = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_user')
     message = models.TextField(max_length=255, null=True, blank=True)
     created = models.DateTimeField()