from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, order_history

router = DefaultRouter()
router.register('', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('order-history/', order_history)
]
