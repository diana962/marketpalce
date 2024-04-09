from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CartItem
from product.models import Clothes
from .serializers import CartItemSerializer


class AddToCartView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = Clothes.objects.get(pk=product_id)
        serializer.save(user=self.request.user, product=product)


class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = CartItem.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Removed'})


class ViewCartView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_price = sum(item.product.price * item.quantity for item in queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'cart_items': serializer.data, 'total_price': total_price})
