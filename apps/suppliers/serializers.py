from rest_framework import serializers
from .models import Supplier, SupplierInventory

class SupplierInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierInventory
        fields = [
            'id', 'supplier', 'item_name', 'quantity', 'unit', 
            'price', 'last_updated', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'last_updated', 'created_at', 'updated_at']

class SupplierSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    inventory = SupplierInventorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Supplier
        fields = [
            'id', 'user', 'user_name', 'user_phone', 'price_prediction_model',
            'total_items', 'last_restocked', 'delivery_radius_km',
            'latitude', 'longitude', 'inventory', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']