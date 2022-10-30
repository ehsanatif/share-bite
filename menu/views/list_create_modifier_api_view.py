from menu.models import Modifiers
from menu.serializers import ModifierSerializer
from rest_framework import generics


class ModifierList(generics.ListCreateAPIView):
    """
    List all Modifiers, or create a new Modifier.
    """
    queryset = Modifiers.objects.all()
    serializer_class = ModifierSerializer
