from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Help Django with our custom user model"""

    def create_user(self,email,name,password = None):
        """Create a new user profile object"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name = name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser():
        """Create and save a new superuser"""
        user = self.create_user(email, name , password)
        user.is_superuser = True
        user.is_staff = True
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """This is used to stroe user profile"""
    email = models.EmailField(max_length =255, unique = True)
    name = models.EmailField(max_length=255)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """get full name of user"""
        return self.name


    def get_Short_name(self):
        """get first name of user"""
        return self.name
    def __str__(self):
        return self.email
