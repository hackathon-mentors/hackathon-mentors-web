from django import forms
from allauth.account.forms import SignupForm

from django.utils.translation import gettext_lazy as _


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