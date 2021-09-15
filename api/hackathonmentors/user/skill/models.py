from django.db import models

from user.models import CustomUser as User


class Skill(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.user}, {self.skill} ({self.proficiency})"
