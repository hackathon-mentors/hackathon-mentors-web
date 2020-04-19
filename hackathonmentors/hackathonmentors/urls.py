from django.contrib import admin
from django.urls import include, path

from hackathonmentors import views

urlpatterns = [
    # path('', 

    path('admin/', admin.site.urls),
]
