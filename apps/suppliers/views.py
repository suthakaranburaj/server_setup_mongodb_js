from rest_framework.decorators import api_view
from apps.common.utils import send_response
from rest_framework import status

@api_view(['GET'])
def supplier_list(request):
    """Get supplier list - placeholder endpoint"""
    return send_response(
        success=True,
        message="Supplier list fetched",
        status_code=status.HTTP_200_OK
    )

@api_view(['POST'])
def create_supplier(request):
    """Create supplier - placeholder endpoint"""
    return send_response(
        success=True,
        message="Supplier created",
        status_code=status.HTTP_201_CREATED
    )