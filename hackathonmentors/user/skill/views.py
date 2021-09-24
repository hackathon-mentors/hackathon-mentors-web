from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from user.skill.models import Skill, UserSkill
from user.skill.serializers import SkillSerializer, UserSkillSerializer


class SkillListCreateAPIView(ListCreateAPIView):
    model = Skill
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class UserSkillListCreateAPIView(ListCreateAPIView):
    model = UserSkill
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


class UserSkillRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    model = UserSkill
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    permission_classes = [IsAuthenticated]
