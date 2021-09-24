from django.db import models


class Hackathon(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)  # make sure NULL passed when is_remote
    is_remote = models.BooleanField(default=False)
    starts = models.DateTimeField()
    ends = models.DateTimeField()

    slug = models.CharField(max_length=64, blank=True)
    verified = models.BooleanField(default=False)

    link = models.CharField(max_length=128, blank=True, null=True)
    img = models.CharField(max_length=256, blank=True, null=True)

    added_by = models.ForeignKey('user.CustomUser', on_delete=models.SET(1))
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        loc = "Remote" if self.is_remote else self.location
        return f"{self.name} ({loc}), {self.starts} - {self.ends}"
        
    class Meta:
        db_table = 'hackathons'
