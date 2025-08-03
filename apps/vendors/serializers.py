from rest_framework import serializers
from .models import Vendor, VendorOrderTracking

class VendorSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    
    class Meta:
        model = Vendor
        fields = [
            'id', 'user', 'user_name', 'user_phone', 'can_order_supply',
            'payment_methods', 'total_orders', 'pending_orders',
            'feedback_qr_code', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class VendorOrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorOrderTracking
        fields = ['id', 'vendor', 'order_id', 'status', 'estimated_delivery', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']