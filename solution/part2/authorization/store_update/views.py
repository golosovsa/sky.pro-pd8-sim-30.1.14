from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from store_update.models import Store
from store_update.serializers import StoreSerializer


class StoreUpdateView(UpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminUser]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)