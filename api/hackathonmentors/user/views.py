from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from allauth.account import views as allauth
from hackathonmentors.views import BaseView
from user.forms import HMUserEditForm
from user.models import CustomUser


class UserDashboardView(BaseView):
    template_name = "dashboard/home.html"


class UserEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = HMUserEditForm
    template_name = "user/edit.html"
    success_url = reverse_lazy("user_dashboard")
    login_url = reverse_lazy("account_login")
    redirect_field_name = "next"

    def get_object(self):
        return self.request.user


"""
Overrides django-allauth's view implementations.
https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py
"""


class HMLoginView(allauth.LoginView):
    template_name = "user/login.html"


class HMSignupView(allauth.SignupView):
    template_name = "user/signup.html"


class HMConfirmEmailView(allauth.ConfirmEmailView):
    template_name = "user/email_confirm.html"


class HMEmailView(allauth.EmailView):
    template_name = "user/email.html"


class HMPasswordChangeView(allauth.PasswordChangeView):
    template_name = "user/password_change.html"


class HMPasswordSetView(allauth.PasswordSetView):
    template_name = "user/password_set.html"


class HMPasswordResetView(allauth.PasswordResetView):
    template_name = "user/password_reset.html"


class HMPasswordResetDoneView(allauth.PasswordResetDoneView):
    template_name = "user/password_reset_done.html"


class HMPasswordResetFromKeyView(allauth.PasswordResetFromKeyView):
    template_name = "user/password_reset_from_key.html"


class HMPasswordResetFromKeyDoneView(allauth.PasswordResetFromKeyDoneView):
    template_name = "user/password_reset_from_key_done.html"


class HMLogoutView(allauth.LogoutView):
    template_name = "user/logout.html"


class HMAccountInactiveView(allauth.AccountInactiveView):
    template_name = "user/account_inactive.html"


class HMEmailVerificationSentView(allauth.EmailVerificationSentView):
    template_name = "user/verification_sent.html"
