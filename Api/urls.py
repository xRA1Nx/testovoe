from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutoModelView, AutoMarkView, ColorView, OrderView
from .yasg import urlpatterns as docs

router = DefaultRouter()
router.register(r'models', AutoModelView)
router.register(r'marks', AutoMarkView)
router.register(r'colors', ColorView)
router.register(r'orders', OrderView)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += docs
