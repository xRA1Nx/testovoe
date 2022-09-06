from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutoModelsView
from .yasg import urlpatterns as docs

router = DefaultRouter()
router.register(r'models', AutoModelsView)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += docs
