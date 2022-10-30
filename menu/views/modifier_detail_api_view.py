from menu.models import Modifiers
from menu.serializers import ModifierSerializer
from rest_framework import generics


class ModifierDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a Modifier instance.
    """
    queryset = Modifiers.objects.all()
    serializer_class = ModifierSerializer
