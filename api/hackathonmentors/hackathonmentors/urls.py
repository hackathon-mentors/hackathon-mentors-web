from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

from rest_framework import routers

from hackathonmentors import views
from hackathon import views as hackathons

router = routers.DefaultRouter()
router.register(r'hackathons', hackathons.HackathonViewSet)


urlpatterns = [
    path('', views.BaseView.as_view(template_name="index.html"), name="index"),
    path('api/', include(router.urls)),
    path('code-of-conduct', views.BaseView.as_view(template_name="coc.html"), name="coc"),
    path('user/', include('user.urls')),
    path('hackathons/', include('hackathon.urls')),
    path('mentors/', include('mentor.urls')),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('img/favicon.ico'))),
]
