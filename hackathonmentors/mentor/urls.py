from django.urls import path

from mentor import views

urlpatterns = [
    path('', views.MentorListView.as_view(), name='mentor_list'),
    path('register/', views.MentorRegistrationView.as_view(), name='mentor_register'),
    path('<slug:slug>/', views.MentorDetailsView.as_view(), name='mentor_view')
]
