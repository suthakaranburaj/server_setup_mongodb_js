from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from apps.common.utils import validate_phone

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    pin = serializers.CharField(write_only=True, min_length=4)
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['name', 'phone', 'pin', 'role', 'image']
    
    def validate_phone(self, value):
        if not validate_phone(value):
            raise serializers.ValidationError("Invalid phone number")
        
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("User already exists, please login")
        
        return value
    
    def validate_pin(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("PIN must be at least 4 characters long")
        return value
    
    def create(self, validated_data):
        pin = validated_data.pop('pin')
        user = User(**validated_data)
        user.set_password(pin)  # This hashes the PIN
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    pin = serializers.CharField()
    
    def validate_phone(self, value):
        if not validate_phone(value):
            raise serializers.ValidationError("Invalid phone number")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'role', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']