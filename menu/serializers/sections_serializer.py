from rest_framework import serializers
from menu.models import Sections


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['id', 'section_name', 'description']
