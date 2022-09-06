from rest_framework.viewsets import ModelViewSet
from .models import AutoModel
from .serializers import AutoModelSerializer


class AutoModelsView(ModelViewSet):
    queryset = AutoModel.objects.all()
    serializer_class = AutoModelSerializer
