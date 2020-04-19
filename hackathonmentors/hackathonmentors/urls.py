from django.contrib import admin
from django.urls import include, path

from hackathonmentors import views

urlpatterns = [
    path('', views.BaseView.as_view(template_name="index.html")),

    path('admin/', admin.site.urls),
]
