from django.db import models


class Hackathon(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    starts = models.DateTimeField()
    ends = models.DateTimeField()

    slug = models.CharField(max_length=64, blank=True)
    verified = models.BooleanField(default=False)

    added_by = models.ForeignKey('user.CustomUser', on_delete=models.SET(1))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.location}), {self.starts} - {self.ends}"

    class Meta:
        db_table = 'hackathons'
