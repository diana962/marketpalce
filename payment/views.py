from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Payment
from .send_mail import send_mail_payment
from .serializers import PaymentSerializer


class PaymentCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        # payment_amount = serializer.validated_data['total_amount']
        # user_balance = user.balance

        # if payment_amount > user_balance:
        #     return Response({'message': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)
        send_mail_payment(user)
        serializer.save(user=user)

class PaymentSuccessView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)