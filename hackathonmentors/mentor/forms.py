from django.forms import ModelForm
from mentor.models import Mentor


class MentorRegistrationForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['name', 'github', 'job_title', 'skills']
