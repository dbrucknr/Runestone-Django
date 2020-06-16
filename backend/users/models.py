from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Overide traditional Django User Model. To be used in the implementation of Social-Login (django-allauth).
    """
    pass