from rest_framework.generics import ListAPIView

from store_list.models import Store
from store_list.serializers import StoreSerializer


# TODO добавьте необходимый код ниже
class StoreListView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
