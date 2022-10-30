from menu.models import Items
from menu.serializers import ItemSerializer
from rest_framework import generics


class ItemList(generics.ListCreateAPIView):
    """
    List all Items, or create a new Item.
    """
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
