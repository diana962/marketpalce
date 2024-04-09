from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'timestamp', 'user', 'address', 'visa', 'visa_password', 'amount')
        read_only_fields = ('id', 'timestamp', 'user', 'amount')
