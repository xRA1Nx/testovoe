import django_filters
from django.db.models import Sum, Case, When
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import AutoModel, AutoMark, Color, Order
from .serializers import AutoModelSerializer, AutoMarkSerializer, \
    ColorSerializer, OrderSerializer, AutoMarkAddSerializer
from .paginators import OrderPagination
from .filters import OrderFilterApi


class AutoModelView(ModelViewSet):
    queryset = AutoModel.objects.all()
    serializer_class = AutoModelSerializer


class AutoMarkView(ModelViewSet):
    queryset = AutoMark.objects.annotate(ordered_cars=Sum('model__order__count'))
    serializer_class = AutoMarkSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AutoMarkSerializer
        else:
            return AutoMarkAddSerializer


class ColorView(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                GenericViewSet):
    queryset = Color.objects.annotate(ordered_cars=Sum('order__count'))
    serializer_class = ColorSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all().order_by('-count')
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['model__automark']
    filterset_class = OrderFilterApi


