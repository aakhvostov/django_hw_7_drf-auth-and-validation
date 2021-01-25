from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from advertisements.classes import NewViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsAuthorEntryOrStuff
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(NewViewSet):
    """ViewSet для объявлений."""

    ordering = '-created_at'
    queryset = Advertisement.objects.order_by(ordering).all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {'post': [IsAuthenticated],
                                    'update': [IsAuthorEntryOrStuff],
                                    'partial_update': [IsAuthorEntryOrStuff],
                                    'destroy': [IsAuthorEntryOrStuff],
                                    'put': [IsAuthorEntryOrStuff]}


# class AdvertisementViewSet(ModelViewSet):
#     """ViewSet для объявлений."""
#
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = AdvertisementFilter
#
#     def get_permissions(self):
#         """Получение прав для действий."""
#         if self.action in ["create", "update", "partial_update"]:
#             return [IsAuthenticated()]
#         return []
