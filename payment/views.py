from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer


class PaymentCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        payment_amount = serializer.validated_data['amount']
        user_balance = user.balance

        if payment_amount > user_balance:
            return Response({'message': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(user=user)

class PaymentSuccessView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from product.models import Clothes
# from like.models import Favorite
#
#
# class Payment(APIView):
#     def post(self, request):
#         data = request.data
#         user = request.user
#
#         # Check if clothes are in favorites and add them to the cart
#         try:
#             favorite_items = Favorite.objects.filter(owner=user)
#             for favorite_item in favorite_items:
#                 Clothes.objects.get_or_create(owner=user, title=favorite_item.clothes.title, price=favorite_item.clothes.price)
#         except Favorite.DoesNotExist:
#             pass
#
#         # Process payment for all items in the cart
#         try:
#             cart_items = Clothes.objects.filter(owner=user)
#             total_amount = sum(item.price for item in cart_items)
#
#             # Check if the buyer has enough money to complete the purchase
#             if user.balance < total_amount:
#                 return Response({"error": "Insufficient funds."}, status=status.HTTP_402_PAYMENT_REQUIRED)
#
#             # Placeholder for payment processing logic
#             # Assuming payment is successful, deduct the amount from the user's balance and empty the cart
#             user.balance -= total_amount
#             user.save()
#             cart_items.delete()
#
#             return Response({"message": "Payment successful. Cart items purchased.",
#                              "total_amount": total_amount}, status=status.HTTP_200_OK)
#
#         except Clothes.DoesNotExist:
#             return Response({"error": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)
#
