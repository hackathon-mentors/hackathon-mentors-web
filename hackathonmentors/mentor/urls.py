from django.urls import path

from mentor import views

urlpatterns = [
    path('', views.MentorListView.as_view(), name='mentor_list'),
    path('<slug:slug>/', views.MentorDetailsView.as_view(), name='mentor_view')
]
