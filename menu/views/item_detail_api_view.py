from menu.models import Items
from menu.serializers import ItemSerializer
from rest_framework import generics


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a Item instance.
    """
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
