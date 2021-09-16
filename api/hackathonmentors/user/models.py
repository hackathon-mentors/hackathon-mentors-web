from django.contrib.auth.models import AbstractUser
from django.db import models

"""
Overrides Django's basic AbstractUser class if needed
Reference: https://github.com/django/django/blob/master/django/contrib/auth/models.py
"""


class CustomUser(AbstractUser):

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'users'
