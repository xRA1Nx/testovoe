from django_filters import rest_framework as filters
from .models import Order, AutoMark


class OrderFilterApi(filters.FilterSet):
    model__automark = filters.ModelChoiceFilter(queryset=AutoMark.objects.all(), label='Марка')

    class Meta:
        model = Order
        fields = ['model__automark']
