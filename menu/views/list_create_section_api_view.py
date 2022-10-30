from menu.models import Sections
from menu.serializers import SectionSerializer
from rest_framework import generics


class SectionList(generics.ListCreateAPIView):
    """
    List all Sections, or create a new Section.
    """
    queryset = Sections.objects.all()
    serializer_class = SectionSerializer
