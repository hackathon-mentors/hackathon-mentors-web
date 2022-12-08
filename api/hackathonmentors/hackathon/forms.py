from django.db import models
from django import forms
from hackathon.models import Hackathon
from .widgets import DateTimePickerInput

class HMHackathonCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=64, label=("Hackathon Name"))
    location = forms.CharField(max_length=64)  # make sure NULL passed when is_remote
    is_remote = forms.BooleanField(label='Is remote', initial=False, required=False)
    ## TODO DIS MUDAFUKA
    starts = forms.DateTimeField()
    ends = forms.DateTimeField()
    
    
    def __init__(self, user=None, *args, **kwargs):
        self.hackathon = Hackathon
        super().__init__(*args, **kwargs)
        self.fields['starts'].widget = DateTimePickerInput()
        self.fields['ends'].widget = DateTimePickerInput()

    class Meta:
        model = Hackathon
        fields = ['name', 'location', 'is_remote', 'starts', 'ends']
        widgets = {
            'starts' : DateTimePickerInput(),
            'ends' : DateTimePickerInput(),
        }
