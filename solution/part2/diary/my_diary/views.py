from rest_framework.generics import CreateAPIView

from my_diary.models import Mark
from my_diary.serializers import MarkCreateSerializer
from my_diary.permissions import MarkCreatePermission
from rest_framework.permissions import IsAuthenticated


class MarkCreateView(CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkCreateSerializer
    permission_classes = [IsAuthenticated, MarkCreatePermission]
