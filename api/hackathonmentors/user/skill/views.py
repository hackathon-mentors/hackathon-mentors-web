from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework import filters

from user.skill.models import Skill
from user.skill.serializers import SkillSerializer


class SkillListCreateAPIView(ListCreateAPIView):
    model = Skill
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
