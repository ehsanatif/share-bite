from rest_framework import serializers
from menu.models import Sections
from .menu_item_serializer import MenuItemSerializer


class MenuSerializer(serializers.ModelSerializer):
    """
    Serializer to display nested response in all sections
    """

    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Sections
        fields = ['id', 'section_name', 'items']
