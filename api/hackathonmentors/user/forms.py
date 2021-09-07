from django import forms
from allauth.account.forms import SignupForm
from user.models import CustomUser as User

from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field


class HMUserSignupForm(SignupForm):
    # https://github.com/pennersr/django-allauth/blob/master/allauth/account/forms.py#L266

    first_name = forms.CharField(
        max_length=30, label=_("First Name"),
        widget=forms.TextInput(attrs={"type": "text", "size": "30", "placeholder": _('First Name')})
    )
    last_name = forms.CharField(
        max_length=150, label=_("Last Name"),
        widget=forms.TextInput(attrs={"type": "text", "size": "150", "placeholder": _('Last Name')})
    )


class HMUserEditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Row(
            Column(Field('first_name'), css_class="col-6"),
            Column(Field('last_name'), css_class="col-6"),
        ),
        Field('username', css_class='form-control mb-3'),
    )

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
