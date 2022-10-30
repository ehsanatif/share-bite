from rest_framework import serializers
from menu.models import Items, Modifiers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id', 'item_name', 'description',
                  'price', 'from_section', 'modifiers']
