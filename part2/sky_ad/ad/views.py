from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from ad.models import Ad
from ad.permissions import AdUpdatePermission
from ad.serializers import AdSerializer


# TODO добавьте ниже код в соответствии с заданием
class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdUpdatePermission, ]
