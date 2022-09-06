from rest_framework import serializers
from .models import AutoModel

class AutoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoModel
        fields = "__all__"
