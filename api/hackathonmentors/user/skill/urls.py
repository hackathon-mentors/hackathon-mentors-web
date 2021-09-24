from django.urls import path, re_path

from user.skill import views

urlpatterns = [
    path('', views.SkillListCreateAPIView.as_view(), name="skills"),
]
