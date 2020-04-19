from django.shortcuts import render

from allauth.account import views as allauth

"""
Overrides django-allauth's view implementations.
https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py
"""


class HMLoginView(allauth.LoginView):
    pass


class HMSignupView(allauth.SignupView):
    template_name = 'user/signup.html'


class HMConfirmEmailView(allauth.ConfirmEmailView):
    pass


class HMEmailView(allauth.EmailView):
    pass


class HMPasswordChangeView(allauth.PasswordChangeView):
    pass


class HMPasswordSetView(allauth.PasswordSetView):
    pass


class HMPasswordResetView(allauth.PasswordResetView):
    pass


class HMPasswordResetDoneView(allauth.PasswordResetDoneView):
    pass


class HMPasswordResetFromKeyView(allauth.PasswordResetFromKeyView):
    pass


class HMPasswordResetFromKeyDoneView(allauth.PasswordResetFromKeyDoneView):
    pass


class HMLogoutView(allauth.LogoutView):
    pass


class HMAccountInactiveView(allauth.AccountInactiveView):
    pass


class HMEmailVerificationSentView(allauth.EmailVerificationSentView):
    pass

