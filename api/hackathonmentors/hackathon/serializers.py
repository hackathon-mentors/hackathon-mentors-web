from hackathon.models import Hackathon
from rest_framework import serializers


class HackathonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hackathon
        fields = ['name', 'location', 'is_remote', 'starts', 'ends', 'slug', 'verified', 'link', 'img', 'modified']
