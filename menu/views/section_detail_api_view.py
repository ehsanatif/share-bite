from menu.models import Sections
from menu.serializers import SectionSerializer
from rest_framework import generics


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update or delete a Section instance.
    """
    queryset = Sections.objects.all()
    serializer_class = SectionSerializer
