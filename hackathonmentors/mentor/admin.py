from django.contrib import admin
from hackathon.models import Hackathon
from mentor.models import Mentor
from user.models import CustomUser

admin.site.register(Hackathon)
admin.site.register(Mentor)
admin.site.register(CustomUser)
