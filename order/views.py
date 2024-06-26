from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from .models import Order


def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return orders

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

