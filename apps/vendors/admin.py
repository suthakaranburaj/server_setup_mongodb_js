from django.contrib import admin
from .models import Vendor, VendorOrderTracking

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'can_order_supply', 'total_orders', 'pending_orders', 'created_at')
    list_filter = ('can_order_supply', 'created_at')
    search_fields = ('user__name', 'user__phone')
    ordering = ('-created_at',)

@admin.register(VendorOrderTracking)
class VendorOrderTrackingAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'order_id', 'status', 'estimated_delivery', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'vendor__user__name')
    ordering = ('-created_at',)