from django.forms import ModelForm
from mentor.models import Mentor


class MentorRegistrationForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['github', 'job_title']
