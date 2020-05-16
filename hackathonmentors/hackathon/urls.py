from django.urls import path

from hackathon import views

urlpatterns = [
    path('', views.HackathonListView.as_view(), name='hackathon_list'),
    path('new/', views.HackathonCreateView.as_view(), name='hackathon_add'),
    path('<slug:slug>/', views.HackathonDetailsView.as_view(), name='hackathon_view')
]
