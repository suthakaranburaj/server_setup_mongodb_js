from djongo import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel

User = get_user_model()

class Supplier(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supplier_profile')
    price_prediction_model = models.CharField(max_length=255, blank=True, null=True)
    
    # Dashboard stats
    total_items = models.IntegerField(default=0)
    last_restocked = models.DateTimeField(blank=True, null=True)
    
    # Delivery radius
    delivery_radius_km = models.FloatField(default=0)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    
    class Meta:
        db_table = 'suppliers'
    
    def __str__(self):
        return f"Supplier: {self.user.name}"

class SupplierInventory(BaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='inventory')
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'supplier_inventory'
    
    def __str__(self):
        return f"{self.item_name} - {self.supplier.user.name}"