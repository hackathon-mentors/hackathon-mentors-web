from django.urls import path, re_path

from . import views
from importlib import import_module

from django.urls import include, path

from allauth.socialaccount import providers

from django.conf import settings

from django.shortcuts import redirect
from django.contrib.auth import logout

def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect('/')

urlpatterns = [
    path("", views.UserDashboardView.as_view(), name="user_dashboard"),

    path("edit/", views.UserEditView.as_view(), name="user_edit"),

    # allauth overrides
    path("signup/", views.HMSignupView.as_view(), name="account_signup"),
    path("login/", views.HMLoginView.as_view(), name="account_login"),
    path("logout/", logout_view, name="account_logout"),
    path("password/change/", views.HMPasswordChangeView.as_view(),
         name="account_change_password"),
    path("password/set/", views.HMPasswordSetView.as_view(), name="account_set_password"),
    path("inactive/", views.HMAccountInactiveView.as_view(), name="account_inactive"),

    # E-mail
    path("email/", views.HMEmailView.as_view(), name="account_email"),
    path("confirm-email/", views.HMEmailVerificationSentView.as_view(),
         name="account_email_verification_sent"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", views.HMConfirmEmailView.as_view(),
            name="account_confirm_email"),

    # password reset
    path("password/reset/", views.HMPasswordResetView.as_view(),
         name="account_reset_password"),
    path("password/reset/done/", views.HMPasswordResetDoneView.as_view(),
         name="account_reset_password_done"),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
            views.HMPasswordResetFromKeyView.as_view(),
            name="account_reset_password_from_key"),
    path("password/reset/key/done/", views.HMPasswordResetFromKeyDoneView.as_view(),
         name="account_reset_password_from_key_done"),
]

if settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [path('social/', include('allauth.socialaccount.urls'))]

# Provider urlpatterns, as separate attribute (for reusability).
provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + '.urls')
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, 'urlpatterns', None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns
