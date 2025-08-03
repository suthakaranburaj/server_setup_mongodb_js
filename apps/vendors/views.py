from rest_framework.decorators import api_view
from apps.common.utils import send_response
from rest_framework import status

@api_view(['GET'])
def vendor_list(request):
    """Get vendor list - placeholder endpoint"""
    return send_response(
        success=True,
        message="Vendor list fetched",
        status_code=status.HTTP_200_OK
    )

@api_view(['POST'])
def create_vendor(request):
    """Create vendor - placeholder endpoint"""
    return send_response(
        success=True,
        message="Vendor created",
        status_code=status.HTTP_201_CREATED
    )