from rest_framework import serializers
from .models import IOT

class CartItemSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(max_length=200)
    device_current = serializers.IntegerField(required=False, default=1)
    device_voltage = serializers.IntegerField(required=False, default=1)
    device_kw = serializers.IntegerField(required=False, default=1)
    hours = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = IOT
        fields = ('__all__')
