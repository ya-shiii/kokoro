from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """ Creates and saves the new user """
        if not email:
            raise ValueError('Please make sure to enter a valid email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """creates and save a superuser """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ allow to use email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField( max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    mailchimp_id = models.CharField(max_length=200, blank=True, null=True)
    tradegecko_id = models.CharField(max_length=200, blank=True, null=True)
    odoo_id = models.CharField(max_length=200, blank=True, null=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'


class Accounts(models.Model):
    """model for the accounts"""
    type_of_account = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    subscription_status = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
