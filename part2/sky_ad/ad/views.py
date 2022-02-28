from rest_framework.generics import UpdateAPIView

from ad.models import Ad
from ad.serializers import AdSerializer


# TODO добавьте ниже код в соответствии с заданием
class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
