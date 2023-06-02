from django.db import models
from user.skill.models import UserSkill


class Mentor(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)

    user = models.ForeignKey("user.CustomUser", on_delete=models.SET(1))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    skills = models.ManyToManyField(UserSkill, verbose_name=("User skills"), blank=True)
    is_official = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (Github@{self.github}, {self.location})"

    class Meta:
        db_table = "mentors"
