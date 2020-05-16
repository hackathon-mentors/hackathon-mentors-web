from django.urls import path

from hackathon.views import HackathonListView

urlpatterns = [
    path('', HackathonListView.as_view(), name='hackathons_list'),
]
