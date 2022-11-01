from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from my_diary.models import Mark
from my_diary.permissions import MarkCreatePermission
from my_diary.serializers import MarkCreateSerializer


# TODO доработайте класс ниже в соответствии с условиями задания
class MarkCreateView(CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkCreateSerializer
    permission_classes = [IsAuthenticated, MarkCreatePermission, ]
