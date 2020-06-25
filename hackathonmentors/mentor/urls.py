from django.urls import path

from mentor import views

urlpatterns = [
    path('', views.MentorListView.as_view(), name='mentor_list'),
]
