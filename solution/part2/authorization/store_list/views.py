from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from store_list.models import Store
from store_list.serializers import StoreSerializer


class StoreListView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, ]
