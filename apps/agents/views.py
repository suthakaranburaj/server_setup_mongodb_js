from rest_framework.decorators import api_view
from apps.common.utils import send_response
from rest_framework import status

@api_view(['GET'])
def agent_list(request):
    """Get agent list - placeholder endpoint"""
    return send_response(
        success=True,
        message="Agent list fetched",
        status_code=status.HTTP_200_OK
    )

@api_view(['POST'])
def create_agent(request):
    """Create agent - placeholder endpoint"""
    return send_response(
        success=True,
        message="Agent created",
        status_code=status.HTTP_201_CREATED
    )