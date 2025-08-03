from rest_framework import serializers
from .models import Agent, VerifiedSupplier

class VerifiedSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifiedSupplier
        fields = [
            'id', 'agent', 'supplier_id', 'verification_date', 
            'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'verification_date', 'created_at', 'updated_at']

class AgentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_phone = serializers.CharField(source='user.phone', read_only=True)
    verified_suppliers = VerifiedSupplierSerializer(many=True, read_only=True)
    
    class Meta:
        model = Agent
        fields = [
            'id', 'user', 'user_name', 'user_phone', 
            'verified_suppliers', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']