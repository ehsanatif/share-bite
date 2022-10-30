from rest_framework import serializers
from menu.models import Modifiers


class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifiers
        fields = ['id', 'description']
