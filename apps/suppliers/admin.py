from django.contrib import admin
from .models import Supplier, SupplierInventory

class SupplierInventoryInline(admin.TabularInline):
    model = SupplierInventory
    extra = 0

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_items', 'delivery_radius_km', 'last_restocked', 'created_at')
    list_filter = ('created_at', 'last_restocked')
    search_fields = ('user__name', 'user__phone')
    ordering = ('-created_at',)
    inlines = [SupplierInventoryInline]

@admin.register(SupplierInventory)
class SupplierInventoryAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'supplier', 'quantity', 'unit', 'price', 'last_updated')
    list_filter = ('unit', 'last_updated', 'created_at')
    search_fields = ('item_name', 'supplier__user__name')
    ordering = ('-last_updated',)