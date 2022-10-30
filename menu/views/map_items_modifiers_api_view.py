from menu.models import Items, Modifiers
from menu.serializers import ItemSerializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response


class MapItems(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    To map modifiers to the item if item already exist else create a new item
    """

    serializer_class = ItemSerializer

    def post(self, request, *args, **kwargs):
        existing_item = Items.objects.filter(
            item_name=request.data['item_name']).first()

        modifier_arr = []
        for modifier_id in request.data['modifiers']:
            mod_obj, created = Modifiers.objects.get_or_create(
                id=modifier_id, description='deafult_name_here')
            modifier_arr.append(mod_obj)

        if existing_item:
            existing_item.modifiers.set(modifier_arr)
            existing_item.save()
            return Response(data=ItemSerializer(existing_item).data, status=status.HTTP_200_OK)
        else:
            return self.create(request, *args, **kwargs)
