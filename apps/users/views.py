from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, get_user_model
from apps.common.utils import send_response, generate_access_token, generate_refresh_token
from apps.common.cloudinary_utils import upload_to_cloudinary
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
import tempfile
import os

User = get_user_model()

@api_view(['GET'])
@permission_classes([AllowAny])
def user_list(request):
    """Get user details - placeholder endpoint"""
    return send_response(
        success=True,
        message="User details fetched",
        status_code=status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Register a new user"""
    try:
        serializer = UserRegistrationSerializer(data=request.data)
        
        if not serializer.is_valid():
            return send_response(
                success=False,
                message="Validation failed",
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        # Handle image upload if present
        image_url = None
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            
            # Save temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{image_file.name.split(".")[-1]}') as temp_file:
                for chunk in image_file.chunks():
                    temp_file.write(chunk)
                temp_file_path = temp_file.name
            
            try:
                image_url = upload_to_cloudinary(temp_file_path)
            except Exception as e:
                return send_response(
                    success=False,
                    message=f"Image upload failed: {str(e)}",
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        
        # Create user
        validated_data = serializer.validated_data
        if image_url:
            validated_data['image'] = image_url
        
        user = serializer.save()
        
        # Generate tokens
        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)
        
        # Store refresh token
        user.refresh_token = refresh_token
        user.save()
        
        # Prepare response data
        user_data = UserSerializer(user).data
        
        response = send_response(
            success=True,
            message="User registered successfully",
            data=user_data,
            status_code=status.HTTP_201_CREATED
        )
        
        # Set cookies
        response.set_cookie(
            'accessToken',
            access_token,
            httponly=False,
            secure=True,
            samesite='Strict'
        )
        response.set_cookie(
            'refreshToken',
            refresh_token,
            httponly=False,
            secure=True,
            samesite='Strict'
        )
        
        # Add token to response data
        response.data['accessToken'] = access_token
        
        return response
        
    except Exception as e:
        return send_response(
            success=False,
            message=f"Registration failed: {str(e)}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """Login user"""
    try:
        serializer = UserLoginSerializer(data=request.data)
        
        if not serializer.is_valid():
            return send_response(
                success=False,
                message="Validation failed",
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        phone = serializer.validated_data['phone']
        pin = serializer.validated_data['pin']
        
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return send_response(
                success=False,
                message="User does not exist",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        # Check PIN
        if not user.check_password(pin):
            return send_response(
                success=False,
                message="Phone or PIN is incorrect",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        # Generate tokens
        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)
        
        # Store refresh token
        user.refresh_token = refresh_token
        user.save()
        
        # Prepare response data
        user_data = UserSerializer(user).data
        
        response = send_response(
            success=True,
            message="Login successful",
            data=user_data,
            status_code=status.HTTP_200_OK
        )
        
        # Set cookies
        response.set_cookie(
            'accessToken',
            access_token,
            httponly=False,
            secure=True,
            samesite='Strict'
        )
        response.set_cookie(
            'refreshToken',
            refresh_token,
            httponly=False,
            secure=True,
            samesite='Strict'
        )
        
        # Add token to response data
        response.data['accessToken'] = access_token
        
        return response
        
    except Exception as e:
        return send_response(
            success=False,
            message=f"Login failed: {str(e)}",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['PATCH'])
def update_user_details(request):
    """Update user details - placeholder endpoint"""
    return send_response(
        success=True,
        message="User details updated",
        status_code=status.HTTP_200_OK
    )