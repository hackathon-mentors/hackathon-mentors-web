from django.urls import path, re_path

from . import views


urlpatterns = [
    path("", views.UserDashboardView.as_view(), name="user_dashboard"),

    # allauth overrides
    path("signup/", views.HMSignupView.as_view(), name="account_signup"),
    path("login/", views.HMLoginView.as_view(), name="account_login"),
    path("logout/", views.HMLogoutView.as_view(), name="account_logout"),
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