from django.contrib.auth.models import AbstractUser
from django.db import models

"""
Overrides Django's basic AbstractUser class if needed
Reference: https://github.com/django/django/blob/master/django/contrib/auth/models.py
"""


class CustomUser(AbstractUser):

    class Meta:
        db_table = 'users'


class Skill(models.Model):
    name = models.CharField(max_length=32)


class UserSkill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    competency = models.PositiveSmallIntegerField()
