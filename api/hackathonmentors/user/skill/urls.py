from django.urls import path, re_path

from user.skill import views

urlpatterns = [
    path('<str:prefix>', views.SkillView.as_view(), name="skill"),
]
