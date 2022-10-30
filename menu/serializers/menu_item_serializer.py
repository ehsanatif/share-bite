from rest_framework import serializers
from menu.models import Items


class MenuItemSerializer(serializers.ModelSerializer):
    """
    Item Serializer to for nested response display in menu(Sections)
    """
    class Meta:
        model = Items
        fields = ['id', 'item_name', 'modifiers']
        depth = 1
