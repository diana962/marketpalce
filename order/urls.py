from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, order_history

router = DefaultRouter()
router.register('', OrderViewSet)
router.register('order-history/', order_history)

urlpatterns = [
    path('', include(router.urls)),
]
