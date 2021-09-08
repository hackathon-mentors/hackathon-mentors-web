from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from user.skill.models import Skill


# Create your views here.
class SkillView(ListView):
    model = Skill

    def get_queryset(self):
        prefix = self.kwargs.get('prefix')

        if prefix:
            return Skill.objects.filter(name__startswith=prefix).order_by('name')

        return Skill.objects.all()

    def get(self, request, *args, **kwargs):
        return HttpResponse(
            serialize("json", self.get_queryset()),
            content_type='application/json'
        )
