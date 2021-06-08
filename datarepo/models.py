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


class contacts(models.Model):
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.IntegerField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.contact_name


class chats(models.Model):
    contact_number = models.ForeignKey(contacts, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(max_length=255, null=True, blank=True)
    created = models.DateTimeField()


class status(models.Model):
    contact_number = models.ForeignKey(contacts, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField()
    created = models.DateTimeField()


class groups(models.Model):
    contact_number = models.ManyToManyField(contacts)
    group_name = models.CharField(max_length=255, null=True, blank=True)
    group_image = models.ImageField()
    description = models.TextField(null=True, blank=True)
    message = models.TextField(max_length=255, null=True, blank=True)
    created = models.DateTimeField()
