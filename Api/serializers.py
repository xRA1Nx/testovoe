from rest_framework import serializers
from .models import AutoModel, AutoMark, Color, Order


class TotalCarsByColorSerializer(serializers.ModelSerializer):
    cars = serializers.IntegerField(read_only=True)

    class Meta:
        model = Color
        # fields = ['name', 'cars']
        fields = '__all__'


class ModelForMark(serializers.ModelSerializer):
    class Meta:
        model = AutoModel
        fields = ['name', ]


class AutoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoModel
        fields = "__all__"


class AutoMarkSerializer(serializers.ModelSerializer):
    model = serializers.SlugRelatedField(slug_field="name", read_only=True)
    ordered_cars = serializers.IntegerField(read_only=True)

    class Meta:
        model = AutoMark
        fields = "__all__"


class AutoMarkAddSerializer(serializers.ModelSerializer):
    model = ModelForMark

    class Meta:
        model = AutoMark
        fields = "__all__"

    # def create(self, validated_data):
    #     m = AutoMark.objects.create(**validated_data)
    #     return m
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', None)
    #     instance.model = validated_data.get('model', None)
    #     instance.save()
    #     return instance


class ColorSerializer(serializers.ModelSerializer):
    ordered_cars = serializers.IntegerField(read_only=True)

    class Meta:
        model = Color
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
