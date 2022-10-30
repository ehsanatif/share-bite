from menu.models import Sections
from menu.serializers import MenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MenutList(APIView):
    """
    List menu with all the sections and their respective items and modifiers.
    """

    def get(self, request):
        sections = Sections.objects.all()
        serializer = MenuSerializer(sections, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
