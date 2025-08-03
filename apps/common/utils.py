import re
import jwt
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

def validate_phone(phone):
    """Validate Indian phone number"""
    if not phone:
        return False
    
    # Remove spaces and dashes
    cleaned = re.sub(r'[\s-]', '', phone)
    
    # Indian phone number regex
    regex = r'^(?:\+91|91|0)?[6-9]\d{9}$'
    
    return bool(re.match(regex, cleaned))

def validate_email(email):
    """Validate email address"""
    if not email:
        return False
    
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))

def send_response(success=True, data=None, message="", status_code=status.HTTP_200_OK):
    """Standardized API response format"""
    return Response({
        'status': success,
        'success': success,
        'data': data,
        'message': message,
    }, status=status_code)

def generate_access_token(user):
    """Generate JWT access token"""
    payload = {
        'user_id': str(user.id),
        'role': user.role,
        'exp': timezone.now() + timedelta(seconds=settings.ACCESS_TOKEN_EXPIRY)
    }
    return jwt.encode(payload, settings.ACCESS_TOKEN_SECRET, algorithm='HS256')

def generate_refresh_token(user):
    """Generate JWT refresh token"""
    payload = {
        'user_id': str(user.id),
        'role': user.role,
        'token_version': getattr(user, 'token_version', 0),
        'exp': timezone.now() + timedelta(seconds=settings.REFRESH_TOKEN_EXPIRY)
    }
    return jwt.encode(payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256')

from django.utils import timezone
from datetime import timedelta