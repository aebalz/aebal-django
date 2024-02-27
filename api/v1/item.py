from api.models import Item
from api.serializer import ItemSerializer
from rest_framework.viewsets import ModelViewSet


class ItemModelViewSet(ModelViewSet):
    queryset = Item.objects
    serializer_class = ItemSerializer
    # metadata_class = APIRootMetadata