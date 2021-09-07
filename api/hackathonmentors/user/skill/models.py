from django.db import models

from hackathonmentors.user.models import CustomUser as User


class Skill(models.Model):
    name = models.CharField(max_length=32)


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    competency = models.PositiveSmallIntegerField()
