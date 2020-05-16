from django.urls import path

from hackathon import views

urlpatterns = [
    path('', views.HackathonListView.as_view(), name='hackathon_list'),
]
