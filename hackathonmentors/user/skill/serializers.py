from rest_framework import serializers
from user.skill.models import Skill, UserSkill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = ('id', 'proficiency', 'skill')
        depth = 1
