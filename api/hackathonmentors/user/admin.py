from django.contrib import admin

from user.models import CustomUser
from user.skill.models import Skill, UserSkill

admin.site.register(CustomUser)
admin.site.register(Skill)
admin.site.register(UserSkill)
