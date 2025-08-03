from djongo import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel

User = get_user_model()

class Vendor(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    can_order_supply = models.BooleanField(default=True)
    payment_methods = models.JSONField(default=list)
    
    # Dashboard stats
    total_orders = models.IntegerField(default=0)
    pending_orders = models.IntegerField(default=0)
    
    feedback_qr_code = models.URLField(blank=True, null=True)
    
    class Meta:
        db_table = 'vendors'
    
    def __str__(self):
        return f"Vendor: {self.user.name}"

class VendorOrderTracking(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='order_tracking')
    order_id = models.CharField(max_length=100)  # Reference to order
    status = models.CharField(max_length=50)
    estimated_delivery = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'vendor_order_tracking'
    
    def __str__(self):
        return f"Order {self.order_id} - {self.status}"