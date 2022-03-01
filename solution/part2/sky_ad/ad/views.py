from rest_framework.generics import UpdateAPIView

from ad.models import Ad
from ad.permissions import IsOwner
from ad.serializers import AdSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsOwner]
